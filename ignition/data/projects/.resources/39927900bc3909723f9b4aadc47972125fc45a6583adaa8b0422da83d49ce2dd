import copy

def deep_merge(dest, src):
    """
    Return a new dictionary that is the deep merge of *dest* and *src*.

    *dest* is **not** modified; a deep copy is made first.
    The merge semantics are identical to the in‑place version:
      * If a key exists in both dicts and both values are dicts,
        they are merged recursively.
      * Otherwise the value from *src* overwrites/creates the key
        in the new dictionary.
    """
    result = copy.deepcopy(dest)

    _recursive_merge(result, src)

    return result


def recursive_merge(target, source):
    """
    Helper that mutates *target* in‑place, merging *source* into it.
    """
    for key, value in source.items():
        if (key in target
                and isinstance(target[key], dict)
                and isinstance(value, dict)):
            # Both are dicts → merge recursively
            recursive_merge(target[key], value)
        else:
            target[key] = value
