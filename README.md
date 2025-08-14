# GitHub Actions Caching & Artifacts Demo

This project demonstrates how to use GitHub Actions caching and artifacts with a simple Python example.

## Features
- **Caching**: Speed up workflow runs by caching dependencies.
- **Artifacts**: Upload and download build/test results between jobs.

## Structure
- `main.py`: Simple Python script.
- `requirements.txt`: Python dependencies.
- `.github/workflows/demo.yml`: GitHub Actions workflow using cache and artifacts.

## Caching Implementation Details

This project uses the [actions/cache](https://github.com/actions/cache) action in the workflow to cache Python dependencies installed via `pip`. Caching is implemented as follows:

1. **Cache Key**:  
   The cache key is generated based on the hash of the `requirements.txt` file. This ensures that the cache is reused as long as dependencies do not change. If `requirements.txt` is updated, a new cache will be created.

2. **Cache Paths**:  
   The workflow caches the `.venv` or `~/.cache/pip` directory (depending on the setup), which contains installed Python packages. This avoids re-downloading and re-installing dependencies on every workflow run.

3. **Workflow Steps**:  
   - The workflow first attempts to restore the cache using the generated key.
   - If the cache is found, dependencies are restored from the cache, speeding up the setup.
   - If the cache is not found (e.g., on the first run or after dependency changes), dependencies are installed from scratch and then saved to the cache for future runs.

4. **Example Cache Step** (from `.github/workflows/demo.yml`):
   ```yaml
   - name: Cache pip dependencies
     uses: actions/cache@v3
     with:
       path: ~/.cache/pip
       key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
       restore-keys: |
         ${{ runner.os }}-pip-
   ```

5. **Benefits**:  
   - Reduces workflow execution time by avoiding repeated downloads.
   - Ensures consistent dependency management across workflow runs.

## Usage
1. Push this repo to GitHub.
2. GitHub Actions will run the workflow on push.
3. Inspect workflow runs for cache and artifact usage.

---

**Replace this README with your own details as needed.**
