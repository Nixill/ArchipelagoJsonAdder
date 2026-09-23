from pathlib import Path
from zipfile import ZipFile

from nicegui import ui, app, native
from nicegui.native import NativeConfig, WindowProxy
from nicegui.ui import markdown as md

from fastapi import Request

import webview
from webview import FileDialog

from archipelagojsonadder import zipmanip

@ui.page('/', title='archipelago.json tool')
def main_page(request: Request) -> None:
  if 'pywebview' not in request.headers.get('user-agent', '').lower():
    ui.markdown('Please use the native app to use this program.').default_classes('error')
    return

  apworld_file: ZipFile | None = None

  async def select_file() -> None:
    nonlocal apworld_file

    if apworld_file:
      apworld_file.close()

    window = app.native.main_window
    if not window: return None
    file = await window.create_file_dialog(
      dialog_type=FileDialog.OPEN,
      file_types=('Archipelago World (*.apworld)',)
    )

    if not file:
      file_error.set_content('None').set_visibility(False)
      file_label.set_content('No file loaded.').set_visibility(True)
      return

    file_path = Path(file[0])

    try:
      apworld_file = zipmanip.open_apworld_file(file_path)

  
  md("""This tool exists for a **player** to add an archipelago.json to apworlds for compatibility with AP 0.7.0, among other things.

Please **do not redistribute** any apworlds you modify with this tool, unless the recipient knows what you are doing.

If you are the **creator** of an apworld, please just add archipelago.json to your world's source instead of using this tool.""")

  ui.separator()

  with ui.stepper() as stepper:
    with ui.step('file_picker', 'Select file'):
      md('Please select an apworld file here.')
      file_button = ui.button('Select apworld', on_click=select_file)
      file_label = md('No file is currently selected. Please select an apworld file to begin.')
      file_error = md('(No error.)').set_visibility(False)

app.native.start_args['user_agent'] = 'NiceGUI-Native/1.0 (pywebview)'
ui.run(native=True, dark=True, port=native.find_open_port(), reload=False)