from __future__ import annotations

from .errors import EndpointError

endpoints = {
    'sfw': {
        'waifu': '/waifu',
        'neko': '/neko',
        'shinobu': '/shinobu',
        'megumin': '/megumin',
        'bully': '/bully',
        'cuddle': '/cuddle',
        'cry': '/cry',
        'hug': '/hug',
        'awoo': '/awoo',
        'kiss': '/kiss',
        'lick': '/lick',
        'pat': '/pat',
        'smug': '/smug',
        'bonk': '/bonk',
        'yeet': '/yeet',
        'blush': '/blush',
        'smile': '/smile',
        'wave': '/wave',
        'highfive': '/highfive',
        'handhold': '/handhold',
        'nom': '/nom',
        'bite': '/bite',
        'glomp': '/glomp',
        'slap': '/slap',
        'kill': '/kill',
        'kick': '/kick',
        'happy': '/happy',
        'wink': '/wink',
        'poke': '/poke',
        'dance': '/dance',
        'cringe': '/cringe',
    },
    'nsfw': {
        'waifu': '/waifu',
        'neko': '/neko',
        'trap': '/trap',
        'blowjob': '/blowjob',
    }
}

def endpoint(type: str, category: str):
    try:
        endpoint = type + endpoints[type][category]
    except KeyError:
        raise EndpointError(type, category)
    else:
        return endpoint
