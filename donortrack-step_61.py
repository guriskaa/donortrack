# === Stage 61: Add performance timing for core list and search operations ===
# Project: DonorTrack
import time

def benchmark_list_and_search(self):
    """Measure list and search operation performance."""
    results = {}
    for label, func in [
        ("list_contacts", self.list_contacts),
        ("search_contacts", self.search_contacts),
        ("list_gifts", self.list_gifts),
        ("search_gifts", self.search_gifts),
        ("list_campaigns", self.list_campaigns),
        ("search_campaigns", self.search_campaigns),
        ("list_thank_you_notes", self.list_thank_you_notes),
        ("search_thank_you_notes", self.search_thank_you_notes),
    ]:
        samples = 100
        start = time.perf_counter()
        for _ in range(samples):
            func()
        elapsed = time.perf_counter() - start
        results[label] = round(elapsed / samples * 1000, 3)
    return results

def print_benchmark(self):
    """Print performance timing for core list and search operations."""
    timings = self.benchmark_list_and_search()
    print("DonorTrack Performance Timing (ms per operation):")
    for label, ms in sorted(timings.items()):
        print(f"  {label:30s}: {ms} ms")
    return timings
