import numpy as np
import numpy.ma as ma

# Set print options for clean output formatting
np.set_printoptions(precision=2)

print("=" * 70)
print("DEMONSTRATION: HANDLING MISSING (NaN) & SPECIAL (Inf) VALUES IN NUMPY")
print("=" * 70)

# Sample Dataset: 2D matrix representing 3 sensor readings across 4 time steps
# Contains valid numbers, NaN (missing data), and positive/negative Infinity
raw_data = np.array([
    [10.0,  12.0,  np.nan, 14.0],   # Sensor 1: Has a missing reading
    [20.0,  np.inf, 22.0,  24.0],   # Sensor 2: Has an infinity spike
    [30.0,  32.0,  34.0,  -np.inf]  # Sensor 3: Has a negative infinity drop
])

print("\n--- RAW DATASET ---")
print(raw_data)


# -------------------------------------------------------------------
# METHOD 1: DETECTION (np.isnan, np.isinf, np.isfinite)
# -------------------------------------------------------------------
print("\n" + "=" * 70)
print("1. DETECTION METHODS")
print("WHEN TO USE: When you need to inspect, count, or locate invalid entries.")
print("=" * 70)

is_missing = np.isnan(raw_data)
is_infinite = np.isinf(raw_data)
is_valid = np.isfinite(raw_data)  # True only for normal, real numbers

print("np.isnan()   -> Identifies missing values:\n", is_missing)
print("np.isinf()   -> Identifies infinity values:\n", is_infinite)
print("np.isfinite()-> Identifies valid, usable numbers:\n", is_valid)
print(f"Total invalid entries: {np.sum(~is_valid)}")


# -------------------------------------------------------------------
# METHOD 2: REMOVING / FILTERING (Boolean Indexing)
# -------------------------------------------------------------------
print("\n" + "=" * 70)
print("2. REMOVING / FILTERING METHOD (Boolean Indexing)")
print("WHEN TO USE: When invalid rows/values can be safely purged, and")
print("you do NOT care about preserving array shape or 2D grid structure.")
print("=" * 70)

# Extract only valid finite numbers into a 1D vector
cleaned_1d = raw_data[np.isfinite(raw_data)]

print("Filtered 1D Array (Only Valid Numbers):\n", cleaned_1d)
print("Notice: Shape changed from 2D (3x4) to 1D:", cleaned_1d.shape)


# -------------------------------------------------------------------
# METHOD 3: REPLACING & IMPUTATION (np.nan_to_num & np.where)
# -------------------------------------------------------------------
print("\n" + "=" * 70)
print("3. REPLACING & IMPUTATION METHODS")
print("WHEN TO USE: When you must keep array size intact (e.g., for ML models)")
print("by replacing NaNs/Infs with default constants or mean/median statistics.")
print("=" * 70)

# 3A. np.nan_to_num() -> Quick replacement with specified default constants
replaced_defaults = np.nan_to_num(
    raw_data, 
    nan=0.0,         # Replace NaN with 0.0
    posinf=999.0,    # Replace +Inf with 999.0
    neginf=-999.0    # Replace -Inf with -999.0
)
print("3A. np.nan_to_num() Output:\n", replaced_defaults)

# 3B. np.where() -> Imputing NaNs with the mean of valid entries
valid_mean = np.mean(cleaned_1d)

# Replace NaNs with the mean, replace Infs with 0, keep valid data as-is
imputed_data = np.where(np.isnan(raw_data), valid_mean, raw_data)
imputed_data = np.where(np.isinf(imputed_data), 0.0, imputed_data)

print(f"\n3B. Imputed with Mean ({valid_mean:.2f}) & Infs zeroed:\n", imputed_data)


# -------------------------------------------------------------------
# METHOD 4: NaN-SAFE AGGREGATIONS (np.nan* functions)
# -------------------------------------------------------------------
print("\n" + "=" * 70)
print("4. NaN-SAFE AGGREGATION FUNCTIONS")
print("WHEN TO USE: When computing statistics (mean, sum, max) directly on")
print("raw dirty data without modifying or cleaning the original array.")
print("=" * 70)

dirty_data = np.array([10.0, 20.0, np.nan, 30.0])

print("Standard np.sum()  -> Fails on NaN: ", np.sum(dirty_data))
print("Safe np.nansum()   -> Ignores NaN:  ", np.nansum(dirty_data))
print("Safe np.nanmean()  -> Ignores NaN:  ", np.nanmean(dirty_data))
print("Safe np.nanmax()   -> Ignores NaN:  ", np.nanmax(dirty_data))


# -------------------------------------------------------------------
# METHOD 5: MASKED ARRAYS (np.ma.masked_invalid)
# -------------------------------------------------------------------
print("\n" + "=" * 70)
print("5. MASKED ARRAYS (np.ma.masked_invalid)")
print("WHEN TO USE: In complex data modeling, spatial grids, image processing,")
print("or time-series where indices/coordinates MUST stay aligned.")
print("=" * 70)

# Temporarily mask invalid data without changing the original array shape
masked_grid = ma.masked_invalid(raw_data)

print("Masked Grid Output ('--' represents masked invalid values):\n", masked_grid)
print("\nBoolean Mask Layer:\n", masked_grid.mask)

# Perform math across rows (axis=1) while ignoring bad values
print("\nPer-Sensor Mean (Axis 1):", masked_grid.mean(axis=1))
print("Preserved Shape:", masked_grid.shape)