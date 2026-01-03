"""
# Compatibility wrapper to import common VTK symbols in a way that works
# with both vtkmodules (VTK 9+) and the legacy 'vtk' compatibility layer.
# This helps avoid import failures on newer Python/VTK combinations.

try:
    # VTK 9+ modular imports
    from vtkmodules.vtkRenderingCore import (
        vtkRenderer,
        vtkActor,
        vtkPolyDataMapper,
        vtkTexture,
    )
    from vtkmodules.vtkFiltersSources import vtkPlaneSource
    from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
    # Ensure the OpenGL rendering backend is available (side-effect import)
    import vtkmodules.vtkRenderingOpenGL2  # noqa: F401
    VTK_MODULES = True
except Exception:
    # Fallback to legacy vtk package if vtkmodules imports fail
    import vtk  # type: ignore

    vtkRenderer = vtk.vtkRenderer
    vtkActor = vtk.vtkActor
    vtkPolyDataMapper = vtk.vtkPolyDataMapper
    vtkTexture = vtk.vtkTexture
    vtkPlaneSource = vtk.vtkPlaneSource
    try:
        # Older VTK installs expose the Qt widget here
        from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor  # type: ignore
    except Exception:
        # Last-resort attempt to import the widget from vtkmodules
        from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor  # type: ignore
    VTK_MODULES = False
"""
