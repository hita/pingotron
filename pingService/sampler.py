from .models import *
from urllib.request import urlopen
from django.utils.timezone import now
import time
from datetime import *


def getTimeLabels(samplesPerMinute, deltaMinutes):

    endTime = datetime.now()
    startTime = endTime - timedelta(minutes=deltaMinutes)
    timeLabels = []
    samples = samplesPerMinute*deltaMinutes

    slot = 0
    while (slot < samples):
        timeStep = startTime + timedelta(minutes=(slot / samplesPerMinute))
        timeLabels.append(timeStep)
        slot = slot + 1
    return timeLabels


def prettifyTimeLabels(timeLabels):
    prettyLabels = []
    for timeLabel in timeLabels:
        prettyLabel = timeLabel.strftime("%H:%M")
        prettyLabels.append(prettyLabel)
    return prettyLabels


def getDelay(timeLabel, server):

    lastKnownDelay = False
    record = Register.objects.filter(
        target=server[0],
        date_creation__lte=timeLabel
    ).order_by('-date_creation')
    lastKnownDelay = record[0].delay_ms
    return lastKnownDelay


def getDelayList(timeLabels, server):
    delayList = []
    for timeLabel in timeLabels:
        thisDelay = getDelay(timeLabel, server)
        delayList.append(thisDelay)
    return delayList


def getStatus(timeLabel, server):
    lastKnownStatus = False
    record = Register.objects.filter(
        server=server[0],
        date_creation__lte=timeLabel
    ).order_by('-date_creation')
    lastKnownStatus = record[0].is_active
    return lastKnownStatus


def produceDelayObject():
    
    labels = getTimeLabels(3, 30)
    datasets = []
    servers = Target.objects.all()

    for server in servers:
        
        delayData = []
        for label in labels:
            delay = Register.objects.filter(
                    target=server,
                    date_creation__lt=label
            ).order_by('-date_creation')
            delayData.append(delay[0].delay_ms)

        serverDataset = {
            "label": server.alias,
            "data": delayData,
        }

        datasets.append(serverDataset)

    delayObject = {
        "labels": prettifyTimeLabels(labels),
        "datasets": datasets,
    }
    return delayObject