edit:
	uv run marimo edit

wasm:
	uv run marimo export html-wasm notebooks/rmv.py -o docs/rmv --mode run

serve:
	uv run python -m http.server --directory docs