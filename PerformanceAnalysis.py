import time
import hashlib
import psutil
import os
import pandas as pd

# Define test parameters for performance analysis
test_cases = [
    {"N": 1024, "r": 8, "p": 1, "dklen": 64},
    {"N": 8192, "r": 8, "p": 1, "dklen": 64},
    {"N": 16384, "r": 8, "p": 1, "dklen": 64},
    # {"N": 65536, "r": 8, "p": 1, "dklen": 32},
]

# Define test password and salt
password = b"benchmark_password"
salt = b"benchmark_salt"

# Function to get memory usage in MB
def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)

# Run performance tests
results = []
for test in test_cases:
    start_memory = get_memory_usage()
    start_time = time.time()
    
    # Run scrypt key derivation
    derived_key = hashlib.scrypt(
        password=password,
        salt=salt,
        n=test["N"],
        r=test["r"],
        p=test["p"],
        dklen=test["dklen"]
    )
    
    end_time = time.time()
    end_memory = get_memory_usage()

    # Calculate execution time and memory usage
    execution_time = end_time - start_time
    memory_usage = end_memory - start_memory

    # Store results
    results.append({
        "N Value": test["N"],
        "Execution Time (seconds)": round(execution_time, 6),
        "Memory Usage (MB)": round(memory_usage, 2)
    })

# Convert to DataFrame and print results
df_results = pd.DataFrame(results)
print(df_results)

# Save results to a CSV file
df_results.to_csv("scrypt_performance_results.csv", index=False)

print("Performance analysis completed. Results saved to 'scrypt_performance_results.csv'")
