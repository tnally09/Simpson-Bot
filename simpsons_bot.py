from typing import no_type_check
import discord
import requests
import base64
import re

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} is active'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Help and bot info
    if message.content.__contains__('/help'):
        await message.channel.send("You've been zzzzzzzzzapped by the Simpsons bot." + "\n" + "I am programmed to respond to secret key phrases with" + "\n" + "select Simpsons moments." + "\n" + "Type /any to press the any key for a random meme at any time.")



    # Random meme generator
    if message.content.__contains__('/any'):
        r = requests.get("https://frinkiac.com/api/random")
        if r.status_code == 200:
            json = r.json()
            _, _, season, _, _, _, _, _, _ = map(str, json["Episode"].values())
            season = int(season)
            # Filter out the crap seasons
            # repeat requests until season requirement is met
            while season > 10:
                r = requests.get("https://frinkiac.com/api/random")
                if r.status_code == 200:
                    json = r.json()
                _, _, season, _, _, _, _, _, _ = map(str, json["Episode"].values())
                season = int(season)
            _, episode, timestamp = map(str, json["Frame"].values())
            
            # pull available content array indices from Frinkiac API
            Subtitles = json["Subtitles"]
            full_quote_raw = ""
            for i in Subtitles:
                full_quote_raw = full_quote_raw + str(i['Content']) + " "

            # split quote into multiple lines, no line greater than 20 characters
            quote_split = re.findall(r".{20}\S*", full_quote_raw)
            print(quote_split)
            quote_raw = ""
            for i in quote_split:
                quote_raw = quote_raw + " " + i + " " + "\n"

            
            # convert raw quote into "Simpsons font" on the image
            quote_bytes = quote_raw.encode('ascii')
            base64_bytes = base64.b64encode(quote_bytes)
            base64_quote = base64_bytes.decode('ascii')



            # full URL after base64 conversion
            img = "https://frinkiac.com/meme/" + episode + "/" + timestamp + ".jpg?b64lines=" + base64_quote

            print(episode)
            print(timestamp)

            
                    
        await message.channel.send(img)
        await message.channel.send("------------------" + "\n" + "You pressed the any key. Where's my tab?")

    # ----------------- Preset library ------------------------
    if message.content.__contains__('water'):
        await message.channel.send("https://frinkiac.com/meme/S03E24/930515.jpg?b64lines=IElUJ1MgRFJJTktJTkcgVEhFIFdBVEVSIQ==")
    if message.content.__contains__('zap'):
        await message.channel.send("https://frinkiac.com/meme/S08E15/475424.jpg?b64lines=IFpaWkFQUCE=")
    if message.content.__contains__('factory'):
        await message.channel.send("https://frinkiac.com/meme/S08E23/677743.jpg?b64lines=QU5EIE1ZIFNPTiBCQVJULgogSEUgT1dOUyBBIEZBQ1RPUlkKIERPV05UT1dOLg==")
    if message.content.__contains__('factorio'):
        await message.channel.send("https://frinkiac.com/meme/S08E23/677743.jpg?b64lines=QU5EIE1ZIFNPTiBCQVJULgogSEUgT1dOUyBBIEZBQ1RPUlkKIERPV05UT1dOLg==")
    if message.content.__contains__('safe'):
        await message.channel.send("https://frinkiac.com/meme/S08E23/1276958.jpg?b64lines=IFdFTEwsIEkgRE9OJ1QgTkVFRCBTQUZFVFkKIEdMT1ZFUyBCRUNBVVNFIEknTSBIT01FUgogU0lNUC4uLg==")
    if message.content.__contains__('joe'):
        await message.channel.send("https://frinkiac.com/meme/S04E10/1012777.jpg?b64lines=SEVMTE8sIEpPRS4=")    
    if message.content.__contains__('baby'):
        await message.channel.send("https://frinkiac.com/meme/S07E03/338387.jpg?b64lines=IE9oLCBteSBMb3JkISBTdHVwaWQKIGJhYmllcyBuZWVkIHRoZSBtb3N0CiBhdHRlbnRpb24u")
    if message.content.__contains__('cube'):
        await message.channel.send("https://frinkiac.com/meme/S07E17/583683.jpg?b64lines=IFllYWgtbG8sIE1yLiBCdXJucycKIG9mZmljZS4gCklzIGl0IGFib3V0IG15CiBjdWJlPw==")
    if message.content.__contains__('burg'):
        await message.channel.send("https://frinkiac.com/meme/S07E21/597479.jpg?b64lines=WWVzLCBhbmQgeW91IGNhbGwgdGhlbQogc3RlYW1lZCBoYW1zIGRlc3BpdGUgdGhlCiBmYWN0IHRoZXkgYXJlIG9idmlvdXNseQogZ3JpbGxlZC4=")         
    if message.content.__contains__('beer'):
        await message.channel.send("https://frinkiac.com/meme/S04E16/353485.jpg?b64lines=IEFORCBIRVJFIFdFIEhBVkUgRFVGRi4KIERVRkYgTElURSBBTkQgT1VSIE5FV0VTVAogRkxBVk9SLCBEVUZGIERSWS4=")
    if message.content.__contains__('test'):
        await message.channel.send("https://frinkiac.com/meme/S08E25/251600.jpg?b64lines=VEVTVElORy4=")
    if message.content.__contains__(' neat'):
        await message.channel.send("https://frinkiac.com/meme/S05E19/92625.jpg?b64lines=SSBKVVNUIFRISU5LIFRIRVknUkUgTkVBVA==")
    if message.content.__contains__('potato'):
        await message.channel.send("https://frinkiac.com/meme/S05E19/92625.jpg?b64lines=SSBKVVNUIFRISU5LIFRIRVknUkUgTkVBVA==")
    if message.content.__contains__('license'):
        await message.channel.send("https://frinkiac.com/meme/S06E04/989954.jpg?b64lines=IEkgcmVwZWF0LCB3ZSBhcmUgc29sZCBvdXQKIG9mIEJvcnQgbGljZW5zZSBwbGF0ZXMu")
    if message.content.__contains__('alive'):
        await message.channel.send("https://frinkiac.com/meme/S06E25/730629.jpg?b64lines=IE1BTiBBTElWRSwgVEhFUkUgQVJFIE1FTgogQUxJVkUgSU4gSEVSRS4=")
    if message.content.__contains__(' dead'):
        await message.channel.send("https://frinkiac.com/meme/S06E18/941723.jpg?b64lines=IERvbid0IGNyeSBmb3IgbWUuIEknbQogYWxyZWFkeSBkZWFkLg==")
    if message.content.__contains__(' die'):
        await message.channel.send("https://frinkiac.com/meme/S05E02/561243.jpg?b64lines=IE5PLiBUSEFUJ1MgR0VSTUFOIEZPUgogVEhFLCBCQVJULCBUSEUu")    
    if message.content.__contains__('glasses'):
        await message.channel.send("https://frinkiac.com/meme/S06E07/739505.jpg?b64lines=UFJPQkFCTFkgTUlTU0VTIEhJUyAKT0xEIEdMQVNTRVMu")  
    if message.content.__contains__('chemical'):
        await message.channel.send("https://frinkiac.com/meme/S06E13/1099147.jpg?b64lines=VUgtT0guIEFDSUQgUkFJTiBBR0FJTi4=") 
    if message.content.__contains__('acid'):
        await message.channel.send("https://frinkiac.com/meme/S06E13/1099147.jpg?b64lines=VUgtT0guIEFDSUQgUkFJTiBBR0FJTi4=") 
    if message.content.__contains__(' oil'):
        await message.channel.send("https://frinkiac.com/meme/S06E25/582364.jpg?b64lines=U09PTiBUSEFUIE1JR0hUWSBBUFBBUkFUVVMKV0lMTCBCVVJTVCBGT1JUSCBXSVRIIElUUyAKUFJFQ0lPVVMgRkxVSUQu") 
    if message.content.__contains__('python'):
        await message.channel.send("https://frinkiac.com/meme/S06E22/267967.jpg?b64lines=T0gsIExPT0ssIEhFUkUgQ09NRVMgTFVNUFkKIFRIRSBTQ0hPT0wgU05BS0Uu") 
    if message.content.__contains__('fire'):
        await message.channel.send("https://frinkiac.com/meme/S07E17/402502.jpg?b64lines=QXcuIEp1c3QgbXkgbHVjay4=") 
    if message.content.__contains__('nuclear'):
        await message.channel.send("https://frinkiac.com/meme/S09E19/665414.jpg?b64lines=ICJOVUMtVS1MQVIiISBJVCdTCiBQUk9OT1VOQ0VELCAiTlVDLVUtTEFSLiI=")
    if message.content.__contains__('nuke'):
        await message.channel.send("https://frinkiac.com/meme/S08E07/769401.jpg?b64lines=R09UVEEgTlVLRSBTT01FVEhJTkcu")  
    if message.content.__contains__('whale'):
        await message.channel.send("https://frinkiac.com/img/S08E06/956955.jpg")  
    if message.content.__contains__('wife'):
        await message.channel.send("https://frinkiac.com/img/S08E06/956955.jpg")  
    if message.content.__contains__('luck'):
        await message.channel.send("https://frinkiac.com/meme/S08E06/671987.jpg?b64lines=SSBET04nVCBSRUNBTEwgU0FZSU5HIApHT09EIExVQ0su")  
    if message.content.__contains__(' car '):
        await message.channel.send("https://frinkiac.com/meme/S08E06/620836.jpg?b64lines=SSBTTEVFUCBJTiBBIFJBQ0lORyBDQVIuIApETyBZT1U_IA==")  
    if message.content.__contains__('power'):
        await message.channel.send("https://frinkiac.com/meme/S08E12/1168099.jpg?b64lines=SSBIQVZFIFBPV0VSUy4KUE9MSVRJQ0FMIFBPV0VSUyE=")  
    if message.content.__contains__('bot'):
        await message.channel.send("https://frinkiac.com/meme/S06E04/659308.jpg?b64lines=U2VlIGFsbCB0aGF0IHN0dWZmCmluIHRoZXJlLCBIb21lcj8gVGhhdCdzCndoeSB5b3VyIHJvYm90IG5ldmVyCndvcmtlZC4=")  
    if message.content.__contains__(' lol'):
        await message.channel.send("https://frinkiac.com/meme/S08E15/385918.jpg?b64lines=WU9VIEFSRSBUSEUgTElWSU5HIEVORCE=") 
    if message.content.__contains__(' hah'):
        await message.channel.send("https://frinkiac.com/meme/S08E15/385918.jpg?b64lines=WU9VIEFSRSBUSEUgTElWSU5HIEVORCE=") 
    if message.content.__contains__('matrix'):
        await message.channel.send("https://frinkiac.com/meme/S10E02/749865.jpg?b64lines=VEhFU0UgQkFCSUVTIFdJTEwgQkUgSU4gClNUT1JFUyBXSElMRSBIRSdTIFNUSUxMIApHUkFQUExJTkcgV0lUSCBUSEUKUElDS0xFIE1BVFJJWC4=") 
    if message.content.__contains__('excellent'):
        await message.channel.send("https://frinkiac.com/meme/S02E18/768488.jpg?b64lines=RXhjZWxsZW50Lg==")
    if message.content.__contains__(' art'):
        await message.channel.send("https://frinkiac.com/meme/S02E18/1155653.jpg?b64lines=SSBodW5nIGl0IG9uIG1lIHdhbGwuCg==")
    if message.content.__contains__('shit'):
        await message.channel.send("https://frinkiac.com/meme/S03E16/1097111.jpg?b64lines=RmlkZGxlLWRlZS1kZWUu")


# Replace hashes with a valid Discord bot token
client.run('#####################################')
