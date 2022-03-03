def compare_version(version1: str, version2: str) -> int:
    version_arr1 = [int(x) for x in version1.split(".")]
    version_arr2 = [int(y) for y in version2.split(".")]
    n1, n2 = len(version_arr1), len(version_arr2)
    for i in range(max(n1, n2)):
        i1 = version_arr1[i] if i < n1 else 0
        i2 = version_arr2[i] if i < n2 else 0
        if i1 > i2:
            return 1
        if i1 < i2:
            return -1
    return 0


print(compare_version("1.0.1", "1"))