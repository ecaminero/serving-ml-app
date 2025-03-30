
import tomli  
from pathlib import Path

def get_project_version():
    """Obtiene la versión del proyecto desde pyproject.toml"""
    try:
        current_dir = Path(__file__).parent
        while current_dir != current_dir.parent:  # Hasta llegar a la raíz
            pyproject_path = current_dir / "pyproject.toml"
            if pyproject_path.exists():
                with open(pyproject_path, "rb") as f:
                    pyproject_data = tomli.load(f)
                
                return pyproject_data.get("tool", {}).get("poetry", {}).get("version", "0.0.0")
            current_dir = current_dir.parent
        return "0.0.0" 
    except Exception as e:
        print(f"Error al obtener la versión: {e}")
        return "0.0.0"

# Asigna la versión a una variable en el módulo
__version__ = get_project_version()