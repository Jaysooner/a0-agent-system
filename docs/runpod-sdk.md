# Overview

Get started with setting up your Runpod projects using Python. Depending on the specific needs of your project, there are various ways to interact with the Runpod platform. This guide provides an approach to get you up and running.

## Install the Runpod SDK

Create a Python virtual environment to install the Runpod SDK library. Virtual environments allow you to manage dependencies for different projects separately, avoiding conflicts between project requirements.

To get started, install setup a virtual environment then install the Runpod SDK library.

<Tabs>
  <Tab title="macOS">
    Create a Python virtual environment with [venv](https://docs.python.org/3/library/venv.html):

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
  </Tab>

  <Tab title="Windows">
    Create a Python virtual environment with [venv](https://docs.python.org/3/library/venv.html):

    ```bash
    python -m venv env
    env\Scripts\activate
    ```
  </Tab>

  <Tab title="Linux">
    Create a Python virtual environment with [venv](https://docs.python.org/3/library/venv.html):

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
  </Tab>
</Tabs>

To install the SDK, run the following command from the terminal.

```bash
python -m pip install runpod
```

You should have the Runpod SDK installed and ready to use.

## Get Runpod SDK version

To ensure you've setup your Runpod SDK in Python, choose from one of the following methods to print the Runpod Python SDK version to your terminal.

<Tabs>
  <Tab title="Pip">
    Run the following command using pip to get the Runpod SDK version.

    ```bash
    pip show runpod
    ```

    You should see something similar to the following output.

    ```bash
    runpod==1.7.9
    ```
  </Tab>

  <Tab title="Shell">
    Run the following command from your terminal to get the Runpod SDK version.

    ```bash
    python3 -c "import runpod; print(runpod.__version__)"
    ```
  </Tab>

  <Tab title="Python">
    To ensure you've setup your installation correctly, get the Runpod SDK version. Create a new file called `main.py`. Add the following to your Python file and execute the script.

    ```py
    import runpod

    version = runpod.version.get_version()

    print(f"Runpod version number: {version}")
    ```

    You should see something similar to the following output.

    ```sh
    Runpod version number: 1.X.0
    ```
  </Tab>
</Tabs>

You can find the latest version of the Runpod Python SDK on [GitHub](https://github.com/runpod/runpod-python/releases).

Now that you've installed the Runpod SDK, add your API key.

## Add your API key

Set `api_key` and reference its variable in your Python application. This authenticates your requests to the Runpod platform and allows you to access the [Runpod API](/sdks/python/apis).

```python
import runpod
import os

runpod.api_key = os.getenv("RUNPOD_API_KEY")
```

<Info>
  It's recommended to use environment variables to set your API key. You shouldn't load your API key directly into your code.

  For these examples, the API key loads from an environment variable called `RUNPOD_API_KEY`.
</Info>

Now that you've have the Runpod Python SDK installed and configured, you can start using the Runpod platform.

For more information, see:

* [APIs](/sdks/python/apis)
* [Endpoints](/sdks/python/endpoints)

# API Wrapper

This document outlines the core functionalities provided by the Runpod API, including how to interact with Endpoints, manage Templates, and list available GPUs. These operations let you dynamically manage computational resources within the Runpod environment.

## Get Endpoints

To retrieve a comprehensive list of all available endpoint configurations within Runpod, you can use the `get_endpoints()` function. This function returns a list of endpoint configurations, allowing you to understand what's available for use in your projects.

```python
import runpod
import os

runpod.api_key = os.getenv("RUNPOD_API_KEY")

# Fetching all available endpoints
endpoints = runpod.get_endpoints()

# Displaying the list of endpoints
print(endpoints)
```

## Create Template

Templates in Runpod serve as predefined configurations for setting up environments efficiently. The `create_template()` function facilitates the creation of new templates by specifying a name and a Docker image.

<Tabs>
  <Tab title="Python">
    ```python
    import runpod
    import os

    runpod.api_key = os.getenv("RUNPOD_API_KEY")

    try:
        # Creating a new template with a specified name and Docker image
        new_template = runpod.create_template(name="test", image_name="runpod/base:0.1.0")

        # Output the created template details
        print(new_template)

    except runpod.error.QueryError as err:
        # Handling potential errors during template creation
        print(err)
        print(err.query)
    ```
  </Tab>

  <Tab title="Output">
    ```json
    {
      "id": "n6m0htekvq",
      "name": "test",
      "imageName": "runpod/base:0.1.0",
      "dockerArgs": "",
      "containerDiskInGb": 10,
      "volumeInGb": 0,
      "volumeMountPath": "/workspace",
      "ports": "",
      "env": [],
      "isServerless": false
    }
    ```
  </Tab>
</Tabs>

## Create Endpoint

Creating a new endpoint with the `create_endpoint()` function. This function requires you to specify a `name` and a `template_id`. Additional configurations such as GPUs, number of Workers, and more can also be specified depending your requirements.

<Tabs>
  <Tab title="Python">
    ```python
    import runpod
    import os

    runpod.api_key = os.getenv("RUNPOD_API_KEY")

    try:
        # Creating a template to use with the new endpoint
        new_template = runpod.create_template(
            name="test", image_name="runpod/base:0.4.4", is_serverless=True
        )

        # Output the created template details
        print(new_template)

        # Creating a new endpoint using the previously created template
        new_endpoint = runpod.create_endpoint(
            name="test",
            template_id=new_template["id"],
            gpu_ids="AMPERE_16",
            workers_min=0,
            workers_max=1,
        )

        # Output the created endpoint details
        print(new_endpoint)

    except runpod.error.QueryError as err:
        # Handling potential errors during endpoint creation
        print(err)
        print(err.query)
    ```
  </Tab>

  <Tab title="Output">
    ```json
    {
      "id": "Unique_Id",
      "name": "YourTemplate",
      "imageName": "runpod/base:0.4.4",
      "dockerArgs": "",
      "containerDiskInGb": 10,
      "volumeInGb": 0,
      "volumeMountPath": "/workspace",
      "ports": null,
      "env": [],
      "isServerless": true
    }
    {
      "id": "Unique_Id",
      "name": "YourTemplate",
      "templateId": "Unique_Id",
      "gpuIds": "AMPERE_16",
      "networkVolumeId": null,
      "locations": null,
      "idleTimeout": 5,
      "scalerType": "QUEUE_DELAY",
      "scalerValue": 4,
      "workersMin": 0,
      "workersMax": 1
    }
    ```
  </Tab>
</Tabs>

## Get GPUs

For understanding the computational resources available, the `get_gpus()` function lists all GPUs that can be allocated to endpoints in Runpod. This enables optimal resource selection based on your computational needs.

<Tabs>
  <Tab title="Python">
    ```python
    import runpod
    import json
    import os

    runpod.api_key = os.getenv("RUNPOD_API_KEY")

    # Fetching all available GPUs
    gpus = runpod.get_gpus()

    # Displaying the GPUs in a formatted manner
    print(json.dumps(gpus, indent=2))
    ```
  </Tab>

  <Tab title="Output">
    ```json
    [
      {
        "id": "NVIDIA A100 80GB PCIe",
        "displayName": "A100 80GB",
        "memoryInGb": 80
      },
      {
        "id": "NVIDIA A100-SXM4-80GB",
        "displayName": "A100 SXM 80GB",
        "memoryInGb": 80
      }
      // Additional GPUs omitted for brevity
    ]
    ```
  </Tab>
</Tabs>

## Get GPU by Id

Use `get_gpu()` and pass in a GPU Id to retrieve details about a specific GPU model by its ID. This is useful when understanding the capabilities and costs associated with various GPU models.

<Tabs>
  <Tab title="Python">
    ```python
    import runpod
    import json
    import os

    runpod.api_key = os.getenv("RUNPOD_API_KEY")

    gpus = runpod.get_gpu("NVIDIA A100 80GB PCIe")

    print(json.dumps(gpus, indent=2))
    ```
  </Tab>

  <Tab title="Output">
    ```json
    {
      "maxGpuCount": 8,
      "id": "NVIDIA A100 80GB PCIe",
      "displayName": "A100 80GB",
      "manufacturer": "Nvidia",
      "memoryInGb": 80,
      "cudaCores": 0,
      "secureCloud": true,
      "communityCloud": true,
      "securePrice": 1.89,
      "communityPrice": 1.59,
      "oneMonthPrice": null,
      "threeMonthPrice": null,
      "oneWeekPrice": null,
      "communitySpotPrice": 0.89,
      "secureSpotPrice": null,
      "lowestPrice": {
        "minimumBidPrice": 0.89,
        "uninterruptablePrice": 1.59
      }
    }
    ```
  </Tab>
</Tabs>

Through these functionalities, the Runpod API enables efficient and flexible management of computational resources, catering to a wide range of project requirements.

# Endpoints

This documentation provides detailed instructions on how to use the Runpod Python SDK to interact with various endpoints. You can perform synchronous and asynchronous operations, stream data, and check the health status of endpoints.

## Prerequisites

Before using the Runpod Python, ensure that you have:

* Installed the Runpod Python SDK.
* Configured your API key.

## Set your Endpoint Id

Pass your Endpoint Id on the `Endpoint` class.

```python
import runpod
import os

runpod.api_key = os.getenv("RUNPOD_API_KEY")

endpoint = runpod.Endpoint("YOUR_ENDPOINT_ID")
```

This allows all calls to pass through your Endpoint Id with a valid API key.

In most situations, you'll set a variable name `endpoint` on the `Endpoint` class. This allows you to use the following methods or instances variables from the `Endpoint` class:

* [health](#health-check)
* [purge\_queue](#purge-queue)
* [run\_sync](#run-synchronously)
* [run](#run-asynchronously)

## Run the Endpoint

Run the Endpoint with the either the asynchronous `run` or synchronous `run_sync` method.

Choosing between asynchronous and synchronous execution hinges on your task's needs and application design.

* **Asynchronous methods**: Choose the asynchronous method for handling tasks efficiently, especially when immediate feedback isn't crucial. They allow your application to stay responsive by running time-consuming operations in the background, ideal for:

  * **Non-blocking calls**: Keep your application active while waiting on long processes.
  * **Long-running operations**: Avoid timeouts on tasks over 30 seconds, letting your app's workflow continue smoothly.
  * **Job tracking**: Get a Job Id to monitor task status, useful for complex or delayed-result operations.

* **Synchronous methods**: Choose the synchronous method for these when your application requires immediate results from operations. They're best for:

  * **Immediate results**: Necessary for operations where quick outcomes are essential to continue with your app's logic.
  * **Short operations**: Ideal for tasks under 30 seconds to prevent application delays.
  * **Simplicity and control**: Provides a straightforward execution process, with timeout settings for better operational control.

### Run synchronously

To execute an endpoint synchronously and wait for the result, use the `run_sync` method. This method blocks the execution until the endpoint run is complete or until it times out.

```python
import runpod
import os

runpod.api_key = os.getenv("RUNPOD_API_KEY")

endpoint = runpod.Endpoint("YOUR_ENDPOINT_ID")

try:
    run_request = endpoint.run_sync(
        {
            "prompt": "Hello, world!",
        },
        timeout=60,  # Timeout in seconds.
    )

    print(run_request)
except TimeoutError:
    print("Job timed out.")
```

### Run asynchronously

Asynchronous execution allows for non-blocking operations, enabling your code to perform other tasks while waiting for an operation to complete. Runpod supports both standard asynchronous execution and advanced asynchronous programming with Python's [asyncio](https://docs.python.org/3/library/asyncio.html) framework.

Depending on your application's needs, you can choose the approach that best suits your scenario.

For non-blocking operations, use the `run` method. This method allows you to start an endpoint run and then check its status or wait for its completion at a later time.

#### Asynchronous execution

This executes a standard Python environment without requiring an asynchronous event loop.

<Tabs>
  <Tab title="Python">
    ```python
    import runpod
    import os

    runpod.api_key = os.getenv("RUNPOD_API_KEY")

    input_payload = {"prompt": "Hello, World!"}

    endpoint = runpod.Endpoint("YOUR_ENDPOINT_ID")
    run_request = endpoint.run(input_payload)

    # Initial check without blocking, useful for quick tasks
    status = run_request.status()
    print(f"Initial job status: {status}")

    if status != "COMPLETED":
        # Polling with timeout for long-running tasks
        output = run_request.output(timeout=60)
    else:
        output = run_request.output()
    print(f"Job output: {output}")
    ```
  </Tab>

  <Tab title="Output">
    ```bash
    Initial job status: IN_QUEUE
    Job output: {'input_tokens': 24, 'output_tokens': 16, 'text': ["Hello! How may I assist you today?\n"]}
    ```
  </Tab>
</Tabs>

#### Asynchronous execution with asyncio

Use Python's `asyncio` library for handling concurrent Endpoint calls efficiently. This method embraces Python's asyncio framework for asynchronous programming, requiring functions to be defined with async and called with await. This approach is inherently non-blocking and is built to handle concurrency efficiently.

<Tabs>
  <Tab title="Python">
    ```python
    import asyncio
    import aiohttp
    import os
    import runpod
    from runpod import AsyncioEndpoint, AsyncioJob

    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # For Windows users.


    runpod.api_key = os.getenv("RUNPOD_API_KEY")


    async def main():
        async with aiohttp.ClientSession() as session:
            input_payload = {"prompt": "Hello, World!"}
            endpoint = AsyncioEndpoint("YOUR_ENDPOINT_ID", session)
            job: AsyncioJob = await endpoint.run(input_payload)

            # Polling job status
            while True:
                status = await job.status()
                print(f"Current job status: {status}")
                if status == "COMPLETED":
                    output = await job.output()
                    print("Job output:", output)
                    break  # Exit the loop once the job is completed.
                elif status in ["FAILED"]:
                    print("Job failed or encountered an error.")

                    break
                else:
                    print("Job in queue or processing. Waiting 3 seconds...")
                    await asyncio.sleep(3)  # Wait for 3 seconds before polling again


    if __name__ == "__main__":
        asyncio.run(main())
    ```
  </Tab>

  <Tab title="Output">
    ```bash
    Current job status: IN_QUEUE
    Job in queue or processing. Waiting 3 seconds...
    Current job status: COMPLETED
    Job output: {'input_tokens': 24, 'output_tokens': 16, 'text': ['Hello! How may I assist you today?\n']}
    ```
  </Tab>
</Tabs>

## Health check

Monitor the health of an endpoint by checking its status, including jobs completed, failed, in progress, in queue, and retried, as well as the status of workers.

<Tabs>
  <Tab title="Python">
    ```python
    import runpod
    import json
    import os

    runpod.api_key = os.getenv("RUNPOD_API_KEY")

    endpoint = runpod.Endpoint("gwp4kx5yd3nur1")

    endpoint_health = endpoint.health()

    print(json.dumps(endpoint_health, indent=2))
    ```
  </Tab>

  <Tab title="Output">
    ```bash
    {
      "jobs": {
        "completed": 100,
        "failed": 0,
        "inProgress": 0,
        "inQueue": 0,
        "retried": 0
      },
      "workers": {
        "idle": 1,
        "initializing": 0,
        "ready": 1,
        "running": 0,
        "throttled": 0
      }
    }
    ```
  </Tab>
</Tabs>

## Streaming

To enable streaming, your handler must support the `"return_aggregate_stream": True` option on the `start` method of your Handler. Once enabled, use the `stream` method to receive data as it becomes available.

<Tabs>
  <Tab title="Endpoint">
    ```python
    import runpod

    runpod.api_key = os.getenv("RUNPOD_API_KEY")

    endpoint = runpod.Endpoint("YOUR_ENDPOINT_ID")

    run_request = endpoint.run(
        {
            "input": {
                "prompt": "Hello, world!",
            }
        }
    )

    for output in run_request.stream():
        print(output)
    ```
  </Tab>

  <Tab title="Handler">
    ```python
    from time import sleep
    import runpod


    def handler(job):
        job_input = job["input"]["prompt"]

        for i in job_input:
            sleep(1)  # sleep for 1 second for effect
            yield i


    runpod.serverless.start(
        {
            "handler": handler,
            "return_aggregate_stream": True,  # Ensures aggregated results are streamed back
        }
    )
    ```
  </Tab>
</Tabs>

<Info>
  The maximum size for a payload that can be sent using yield to stream results is 1 MB.
</Info>

## Status

Returns the status of the Job request. Set the `status()` function on the run request to return the status of the Job.

<Tabs>
  <Tab title="Python">
    ```python
    import runpod

    runpod.api_key = os.getenv("RUNPOD_API_KEY")

    input_payload = {"input": {"prompt": "Hello, World!"}}

    endpoint = runpod.Endpoint("YOUR_ENDPOINT_ID")
    run_request = endpoint.run(input_payload)

    # Initial check without blocking, useful for quick tasks
    status = run_request.status()
    print(f"Initial job status: {status}")

    if status != "COMPLETED":
        # Polling with timeout for long-running tasks
        output = run_request.output(timeout=60)
    else:
        output = run_request.output()
    print(f"Job output: {output}")
    print(f"An error occurred: {e}")
    ```
  </Tab>

  <Tab title="Output">
    ```bash
    Initial job status: IN_QUEUE
    Job output: Hello, World!
    ```
  </Tab>
</Tabs>

## Cancel

You can cancel a Job request by using the `cancel()` function on the run request. You might want to cancel a Job because it's stuck with a status of `IN_QUEUE` or `IN_PROGRESS`, or because you no longer need the result.

The following pattern cancels a job given a human interaction, for example pressing `Ctrl+C` in the terminal.

This sends a `SIGINT` signal to the running Job by catching the `KeyboardInterrupt` exception.

<Tabs>
  <Tab title="Python">
    ```python
    import time
    import runpod

    runpod.api_key = os.getenv("RUNPOD_API_KEY")

    input_payload = {
        "messages": [{"role": "user", "content": f"Hello, World"}],
        "max_tokens": 2048,
        "use_openai_format": True,
    }

    try:
        endpoint = runpod.Endpoint("YOUR_ENDPOINT_ID")
        run_request = rp_endpoint.run(input_payload)

        while True:
            status = run_request.status()
            print(f"Current job status: {status}")

            if status == "COMPLETED":
                output = run_request.output()
                print("Job output:", output)

                generated_text = (
                    output.get("choices", [{}])[0].get("message", {}).get("content")
                )
                print(generated_text)
                break
            elif status in ["FAILED", "ERROR"]:
                print("Job failed to complete successfully.")
                break
            else:
                time.sleep(10)
    except KeyboardInterrupt:  # Catch KeyboardInterrupt
        print("KeyboardInterrupt detected. Canceling the job...")
        if run_request:  # Check if a job is active
            run_request.cancel()
        print("Job canceled.")
    ```
  </Tab>

  <Tab title="Output">
    ```bash
    Current job status: IN_QUEUE
    Current job status: IN_PROGRESS
    KeyboardInterrupt detected. Canceling the job...
    Job canceled.
    ```
  </Tab>
</Tabs>

### Timeout

Use the `cancel()` function and the `timeout` argument to cancel the Job after a specified time.

In the previous `cancel()` example, the Job is canceled due to an external condition. In this example, you can cancel a running Job that has taken too long to complete.

<Tabs>
  <Tab title="Python">
    ```python
    from time import sleep
    import runpod
    import os

    runpod.api_key = os.getenv("RUNPOD_API_KEY")

    input_payload = {"input": {"prompt": "Hello, World!"}}

    endpoint = runpod.Endpoint("YOUR_ENDPOINT_ID")


    # Submit the job request
    run_request = endpoint.run(input_payload)

    # Retrieve and print the initial job status
    initial_status = run_request.status()
    print(f"Initial job status: {initial_status}")

    # Attempt to cancel the job after a specified timeout period (in seconds)
    # Note: This demonstrates an immediate cancellation for demonstration purposes.
    # Typically, you'd set the timeout based on expected job completion time.
    run_request.cancel(timeout=3)

    # Wait for the timeout period to ensure the cancellation takes effect
    sleep(3)
    print("Sleeping for 3 seconds to allow for job cancellation...")

    # Check and print the job status after the sleep period
    final_status = run_request.status()
    print(f"Final job status: {final_status}")
    ```
  </Tab>

  <Tab title="Output">
    ```bash
    Initial job status: IN_QUEUE
    Sleeping for 3 seconds to allow for job cancellation...
    Final job status: CANCELLED
    ```
  </Tab>
</Tabs>

## Purge queue

You can purge all jobs from a queue by using the `purge_queue()` function. You can provide the `timeout` parameter to specify how long to wait for the server to respond before purging the queue.

`purge_queue()` doesn't affect Jobs in progress.

```python
import runpod
import os

runpod.api_key = os.getenv("RUNPOD_API_KEY")

endpoint = runpod.Endpoint("YOUR_ENDPOINT_ID")

endpoint.purge_queue(timeout=3)
```
