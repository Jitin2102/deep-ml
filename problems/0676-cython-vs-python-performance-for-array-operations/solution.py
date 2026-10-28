
import math

def analyze_array_performance(n: int, operations: list) -> dict:
    methods = ("python", "cython", "numpy")
    results = []
    totals = {method: 0.0 for method in methods}
    crossover_sizes = {}

    for op in operations:
        name = op["name"]
        times = {}

        for method in methods:
            overhead = op[f"{method}_overhead_ns"]
            per_elem = op[f"{method}_per_elem_ns"]

            time_ns = overhead + n * per_elem
            times[method] = time_ns / 1000
            totals[method] += times[method]

        best = min(methods, key=lambda method: (times[method], method))

        results.append({
            "name": name,
            "python_us": round(times["python"], 2),
            "cython_us": round(times["cython"], 2),
            "numpy_us": round(times["numpy"], 2),
            "cython_speedup": round(
                times["python"] / times["cython"]
                if times["cython"] != 0 else (
                    math.inf if times["python"] > 0 else 1.0
                ), 2
            ),
            "numpy_speedup": round(
                times["python"] / times["numpy"]
                if times["numpy"] != 0 else (
                    math.inf if times["python"] > 0 else 1.0
                ), 2
            ),
            "best": best
        })

        numpy_oh = op["numpy_overhead_ns"]
        cython_oh = op["cython_overhead_ns"]
        numpy_pe = op["numpy_per_elem_ns"]
        cython_pe = op["cython_per_elem_ns"]

        if cython_pe <= numpy_pe:
            crossover = -1
        else:
            ratio = (numpy_oh - cython_oh) / (cython_pe - numpy_pe)
            crossover = 0 if ratio <= 0 else math.ceil(ratio)

        crossover_sizes[name] = crossover

    recommended = min(methods, key=lambda method: (totals[method], method))

    return {
        "operations": results,
        "pipeline_python_us": round(totals["python"], 2),
        "pipeline_cython_us": round(totals["cython"], 2),
        "pipeline_numpy_us": round(totals["numpy"], 2),
        "recommended": recommended,
        "crossover_sizes": crossover_sizes
    }
