#!/usr/bin/env python
import json
from kafka import KafkaProducer
from flask import Flask, request

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:29092')


def log_to_kafka(topic, event):
    event.update(request.headers)
    producer.send(topic, json.dumps(event).encode())

    
@app.route("/")
def default_response():
    default_event = {'event_type': 'default'}
    log_to_kafka('events', default_event)
    return "This is the default response!\n"


@app.route("/purchase_a_long_sword")
def purchase_a_long_sword():
    purchase_long_sword_event = {'event_type': 'purchase_sword',
                                 'sword_type': 'longsword'}
    log_to_kafka('events', purchase_long_sword_event)
    return "Long Sword Purchased!\n"

@app.route("/purchase_a_short_sword")
def purchase_a_short_sword():
    purchase_short_sword_event = {'event_type': 'purchase_sword',
                                  'sword_type': 'shortsword'}
    log_to_kafka('events', purchase_short_sword_event)
    return "Short Sword Purchased!\n"

@app.route("/join_craftman_guild")
def join_craftman_guild():
    join_craftman_guild_event = {'event_type': 'join_guild',
                                 'guild_type': 'craftman_guild'}
    log_to_kafka('events', join_craftman_guild_event)
    return "Joined Craftman Guild!\n"


@app.route("/join_merchant_guild")
def join_merchant_guild():
    join_merchant_guild_event = {'event_type': 'join_guild',
                                  'guild_type': 'merchant_guild'}
    log_to_kafka('events', join_merchant_guild_event)
    return "Joined Merchant Guild!\n"

