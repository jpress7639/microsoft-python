def process_image_metadata(records):
    """Summarize a list of image records.

    Each record should be a dict with keys:
        - "name": str
        - "size_kb": int
        - "tags": list of str

    The function must:
        1. Ignore records missing required keys or with non-integer size_kb.
        2. Compute total and average size over valid records.
        3. Count how many valid images contain each tag.

    Return a dict with keys:
        - "total_size_kb": int
        - "average_size_kb": float
        - "tag_counts": dict mapping tag -> count
    """
    # TODO: implement this function according to the specification
    # Replace the placeholder implementation below.
    total_size = 0
    valid_count = 0
    tag_counts = {}

    for record in records:
        if not all(k in record for k in ("name", "size_kb", "tags")):
            continue
        if not isinstance(record["size_kb"], int):
            continue
        total_size += record["size_kb"]
        valid_count += 1
        for tag in record["tags"]:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

    average_size = total_size / valid_count if valid_count > 0 else 0.0

    return {
        "total_size_kb": total_size,
        "average_size_kb": average_size,
        "tag_counts": tag_counts,
    }

def build_health_report(status_code, response_time_ms):
    """Build a health report for an HTTP endpoint.

    Args:
        status_code (int): HTTP status code from the endpoint.
        response_time_ms (float): Response time in milliseconds.

    Returns:
        dict: A dictionary containing keys:
            - "is_healthy" (bool)
            - "status_code" (int)
            - "response_time_ms" (float, rounded to two decimals)
            - "priority" (str)
    """
    # TODO: Implement the logic described in the prompt.
    # Remember to:
    # 1. Determine health based on status code and response time.
    # 2. Round response_time_ms to two decimal places.
    # 3. Set priority based on health and status code ranges.
    is_healthy = 200 <= status_code < 300 and response_time_ms < 500
    rounded_response_time = round(response_time_ms, 2)
    if not is_healthy:
        if status_code >= 500:
            priority = "high"
        elif 400 <= status_code < 500:
            priority = "medium"
        else:
            priority = "low"
    else:
        priority = "low"
    return {
        "is_healthy": is_healthy,
        "status_code": status_code,
        "response_time_ms": rounded_response_time,
        "priority": priority,
    }

def select_azure_vm_size(cpu_cores, memory_gb):
    """Return a recommended Azure VM size string based on CPU and memory.

    Args:
        cpu_cores (int): Number of CPU cores required.
        memory_gb (int or float): Amount of memory in GB required.

    Returns:
        str: Recommended Azure VM size.
    """
    # TODO: implement the selection rules described in the prompt
    if cpu_cores <= 2 and memory_gb <= 4:
        return "Standard_B1s"
    elif cpu_cores <= 4 and memory_gb <= 8:
        return "Standard_B2s"
    elif cpu_cores <= 8 and memory_gb <= 16:
        return "Standard_D2s_v3"
    elif cpu_cores <= 16 and memory_gb <= 32:
        return "Standard_D4s_v3"
    else:
        return "Standard_D8s_v3"

def estimate_monthly_cost(vm_size, hours_per_month):
    """Estimate the monthly cost in USD for a given Azure VM size.

    Args:
        vm_size (str): Azure VM size name.
        hours_per_month (int or float): Number of hours the VM runs per month.

    Returns:
        float: Estimated monthly cost in USD.
    """
    # TODO: implement the pricing logic described in the prompt
    pricing = {
        "Standard_B1s": 0.012,
        "Standard_B2s": 0.024,
        "Standard_D2s_v3": 0.096,
        "Standard_D4s_v3": 0.192,
        "Standard_D8s_v3": 0.384,
    }
    if vm_size not in pricing:
        # Return 0.0 for unknown VM sizes.
        return 0.0
    hourly_rate = pricing[vm_size]
    return round(hourly_rate * hours_per_month, 2)