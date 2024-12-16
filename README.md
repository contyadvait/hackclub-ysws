# Hack Club YSWS List
Welcome to the actual list of every single Hack Club YSWS (or currently an API of it)! An API also exists for easy addition of new YSWSes

*I know the Mongo key is public, and this is on purpose so deployment works lol*

This will soon become a website (once I finish my 10th grade examinations)

## API
### GET: `/api/all/`
- Get all existing YSWSes
- This will give all the YSWSes in the format below
- Dates will be in **DD/MM/YYYY**

```json
[
    {
        "banner": "",
        "channel": "https://hackclub.slack.com/archives/C07PZMBUNDS",
        "completed": false,
        "end": "31/01/2025",
        "id": "highseas",
        "name": "High Seas",
        "website": "https://highsaes.hackclub.com"
    },
    {
        "banner": "",
        "channel": "https://hackclub.slack.com/archives/C02UN35M7LG",
        "completed": false,
        "end": "never",
        "id": "sprig",
        "name": "Sprig",
        "website": "https://sprig.hackclub.com"
    },
    {
        "banner": "",
        "channel": "https://hackclub.slack.com/archives/C056AMWSFKJ",
        "completed": false,
        "end": "never",
        "id": "onboard",
        "name": "Onboard",
        "website": "https://hackclub.com/onboard"
    },
    {
        "banner": "",
        "channel": "https://hackclub.slack.com/archives/C07F3EA2L8G",
        "completed": false,
        "end": "never",
        "id": "liveonboard",
        "name": "OnBoard Live",
        "website": "https://hackclub.com/onboard"
    },
    {
        "banner": "",
        "channel": "https://hackclub.slack.com/archives/C06UJR8QW0M",
        "completed": false,
        "end": "never",
        "id": "bobadrops",
        "name": "Boba Drops",
        "website": "https://boba.hackclub.com"
    }
]
(and so on...)
```

### GET: `api/[id]/`
- Based on the ID of the YSWS, get the specifics on that YSWS

So for example, for High Seas, access it at `/api/highseas/`:
```json
{
    "banner": "",
    "channel": "https://hackclub.slack.com/archives/C07PZMBUNDS",
    "completed": false,
    "description": "a general purpose YSWS, similar to summer's Arcade",
    "end": "31/01/2025",
    "id": "highseas",
    "name": "High Seas",
    "tagline": "Build, battle, booty, repeat!",
    "we_ship": "Doubloons which you can use to purchase things!",
    "website": "https://highsaes.hackclub.com",
    "you_ship": "Any projects recorded with Hackatime"
}
```

### GET `api/done`
- get all completed YSWSes (with additional details)

---
### POST: `/api/modify`
- POST a json of your new YSWS or modify an existing YSWS through its ID
- Options for `"type"`: `"add"`, `"modify"`, `"delete"`
- example of post: 
```json
{
    "type": "add",
    "ysws": {
        "id": "sprig",
        "name": "Sprig",
        "tagline": "Every player is a creator.",
        "banner": "Link from #cdn",
        "you_ship": "A Sprig game, made in the Sprig engine",
        "we_ship": "A Sprig console",
        "website": "sprig.hackclub.com",
        "completed": false,
        "end": "never"
    }
}
```

### POST: `/api/bulk_add`
- NOT RECCOMENDED FOR NORMAL USE
- this is for adding multiple YSWSes at once
- example of post: refer to default_data.json