# tsukikage_api
月影村API模倣サーバー  
[![pytest](https://github.com/Lucky-Mano/tsukikage_api/actions/workflows/pytest.yml/badge.svg)](https://github.com/Lucky-Mano/tsukikage_api/actions/workflows/pytest.yml)

## TO USE
1. json files in config directory.
2. Edit ShirenV2.exe using binary editor.
  1. Access Server URL is `http://localhost`
  2. Auth URL is `http://localhost/api/auth`

### Use Docker
1. Move this directory.
2. Run `docker-compose up`
3. Run ShirenV2.exe and authenticate.
4. SUCCESS👍

### Use local python
1. Install poetry
2. Run `poetry install`
3. Run `poetry run python app.py`
4. Run ShirenV2.exe and authenticate.
5. SUCCESS👍