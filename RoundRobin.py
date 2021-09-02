def do_processing(job_cc, slice):
    return (job_cc - slice, slice) if (job_cc - slice) >= 0 else (0, job_cc)

def roundRobin(jobs, slice, index):
    current_job_index = 0
    total_cc = 0
    while jobs[index] > 0:
        if jobs[current_job_index] > 0:
            remaining, processed = do_processing(jobs[current_job_index], slice)
            total_cc += processed
            jobs[current_job_index] = remaining

        current_job_index = (current_job_index + 1) if (current_job_index + 1) < len(jobs) else 0
    return total_cc

print(roundRobin([16, 20, 15, 27, 27, 22, 20], 4, 3))