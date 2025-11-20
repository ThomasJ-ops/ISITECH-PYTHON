## Complex nested dictionary in LabEx environment
project_data = {
    "departments": {
        "engineering": {
            "teams": {
                "backend": ["Alice", "Bob"],
                "frontend": ["Charlie", "David"]
            }
        }
    }
}

## Advanced extraction
backend_team = project_data.get("departments", {}) \
    .get("engineering", {}) \
    .get("teams", {}) \
    .get("backend", [])

print(backend_team)