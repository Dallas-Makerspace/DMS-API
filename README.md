# DMS-API
MakerManager, Calendar, Queue, and Inventory API


## Running

1. Install docker for (windows, mac, linux)

2. execute in a bash shell (git bash for windows, xterm/Terminal.app)

```
git clone https://github.com/Dallas-Makerspace/DMS-API
make stack=dmsapi_dev
```

## Notes

Oauth2 authentication is based on https://github.com/pyeve/eve-oauth2 and should be fleshed out.


## Road Map

 - Migrate database schema from https://github.com/Dallas-Makerspace/makermanager4/tree/master/database
 - Migrate database schema from https://github.com/Dallas-Makerspace/calendar/tree/master/src/Model
 - Migrate database schema from https://github.com/Dallas-Makerspace/Inventory/tree/master/src/app/Model
 - Integrate Algoria Search (e.g. https://github.com/armadillica/pillar/blob/master/pillar/__init__.py)
 - Integrate docker hub
 - Auto deployment via communitygrid::shephard
