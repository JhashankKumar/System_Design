Strategies for Handling API Failures in Backend Systems

API failures in backend systems, specifically focusing on microservices.

The core problem discussed is that when a microservice goes down and is restarted, it can immediately crash again if client services are constantly and blindly retrying their failed requests, causing massive traffic spikes. To fix this, several strategies can be applied on both the client (e.g., an Order Service) and the server (e.g., an Inventory Service) sides.

Pre-requisite: Knowing When to Retry
Before implementing retry mechanisms, a system must check the HTTP error codes to determine if a retry is even worthwhile.

Do not retry: 400-level errors (like Bad Request), because sending the same wrong arguments will just result in the same error.

Do retry: 500-level errors (Internal Server Error) or Timeout errors, as the server might recover on a subsequent attempt.

Client-Side Strategies

These are techniques used by the system making the API call (e.g., the Order Service) to handle failures efficiently:

1. Fixed (Blind) Retry
How it works: The system is configured to retry a fixed number of times (e.g., 10 times) immediately after an error occurs.

The Problem: While it works for smaller scales, at large scales, many clients blindly retrying at the same time can put immense pressure on the receiving server, potentially crashing it.

2. Exponential Retry (Backoff)
How it works: Instead of retrying constantly, the client waits for progressively longer periods between each attempt. For example, it might wait 100ms for the first retry, 300ms for the second, and 600ms for the third.

The Problem: Multiple clients might still end up syncing their wait times, sending waves of requests at the exact same 100ms, 300ms, and 600ms marks, which still spikes the server load.

3. Exponential Backoff with Jitter
How it works: To fix the synchronization problem, a random time interval (jitter) is added to the exponential wait time of each client. This ensures that retry requests are distributed randomly, preventing heavy simultaneous loads on the server.

The Problem: If too many API calls fail and wait around, the client system's threads can get stuck waiting. This can eventually cause the client itself (e.g., the Order Service) to run out of threads and crash, even though it was trying to protect the server.

4. Circuit Breaker
How it works: This intelligently tackles the thread-blocking issue. If requests fail consistently (e.g., 200 failed requests in 60 seconds), the circuit "opens" and the client stops calling the server entirely, immediately returning errors to save thread resources.

Recovery: After some time, it slowly attempts to "close" the circuit by letting a small API call through. If it succeeds, the circuit closes and normal traffic resumes; if it fails, it stays open.

5. Message Queue
How it works: Instead of letting threads block and wait during an API failure, the client pushes the failed request into a message queue. Once the destination server is back online, the queue forwards the requests to it, keeping the client safe from crashes.

6. Retry Budgeting
How it works: Used by large companies like Google, this allocates a strict mathematical budget for retries. For instance, out of 10,000 total requests, a system might be allowed a maximum of 200 retries. Once the 200-retry budget is exhausted, the system immediately throws an error instead of making further attempts.

Server-Side Strategies

These are defensive mechanisms used by the receiving server (e.g., the Inventory Service) to protect itself from being overwhelmed:

1. Rate Limiting
How it works: The server sets a hard cap on how many requests it will accept in a given timeframe (e.g., 10,000 requests per second). Any requests beyond this limit, even retries, are rejected.

2. Adaptive Rate Limiting
How it works: Instead of a fixed number, the server dynamically adjusts its rate limit based on its real-time health metrics, like CPU or Memory usage. If the CPU is under heavy load, it might drop the limit from 10,000 requests down to 5,000 or even 200 to keep the system stable.

3. Resource Restriction (Bulkheading)
How it works: The server divides its internal resources (like its thread pool) among different clients. For example, if it has 1000 threads, it might restrict the Order system to only 300 threads and the Customer system to 200 threads. This ensures that if the Order system floods the server with retries, it won't consume resources meant for other systems
