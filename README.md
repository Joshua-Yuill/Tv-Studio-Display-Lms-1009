# 👋 Hi there! What even is this?
So you might be wondering what this repository is about, especially if you found this through idle googling. This repository documents my deep dive into understanding the LMS-1009 Tally Display from 1996 and how it can be used today. I was browsing ebay and found one for sale (for cheap I might add) and I was fascinated on how it could be used, as its 2x 9 character display on the front has a real retro feel that I absolutely love. 
## Disclaimer:
Seriously electricity is dangerous, and I take ZERO responsibility for anything that happens to you or anything else because of YOUR actions. This whole thing should just be taken as a documentation of how I managed to communicate with my display and not as a "How-To". Any electrical or other works should only be undertaken by competent persons only.
## ⚡ So without power this is just an advanced rock.
The first task on receiving the unit was figuring out how to power it as mine did not come with a power adapter, and it was not a standard connector that I could easily replace. If yours came with a power adapter, good news, you can skip this section and move onto the next one! For those in the same boat as me, well let me show you how I got round it.
### It ain't pretty but it'll get the job done
#### Parts List
- 9-12v 4a Ac or Dc PSU - [I used this one here](https://www.amazon.co.uk/Adapter-100-240V-50-60hz-Transformer-5-5x2-5mm-12V-4A-Power-Supply/dp/B0915Y3Y2Q/ref=sr_1_3)
- Solder
#### Tools List
- Soldering Iron
- Side cutters
- Multimeter _(Optional)_

The display takes 9-12v 4a AC or DC. I decided that the easiest way to get power to the display would be to solder directly to the port connector on the PCB.

<img src="https://cdn.discordapp.com/attachments/816645352215150602/1087513696546324480/IMG_20230320_224318.jpg"
     alt="Cables soldered to PCB"
     width="400"/>

Don't forget pull the cable through the case of the device first so the unit can be closed up afterwards. Also I know my soldering is bad, so apologies for that.

<img src="https://cdn.discordapp.com/attachments/816645352215150602/1087512351303020604/IMG_20230320_225050.jpg"
     alt="Cables Through Device Housing"
     width="400"/>

## 🤔It's electrifying! But what now?
Here comes the most time consuming part of this project. Figuring out just how to communicate with the unit. From reading around on the limited documentation available I was able to understand that the device communicated over the RS-422/RS-485 protocol. So I did what any sane person would do, I went to amazon and typed in "Usb to RS-422/RS-485 Converter" and was kind of bewildered by the number of different options and variances that are available. This could be the part where I pretend like I knew what I was doing, but honestly I picked the one that looked the most versatile and was within my budget and waited for it to arrive.
### How do I do this?
#### Parts list
- Usb to RS-422/RS-485 - [I used this one here](https://www.amazon.co.uk/DSD-TECH-SH-U11F-Industrial-Application-White/dp/B083XSG1RG)
- RJ 11 Cable - [I used this one here](https://www.amazon.co.uk/dp/B000MSPID4)

(I can't guarantee that any other adapters or cables will or won't work, I just know these do.)
#### Tools List
- Side cutters
### The Process
First things first was to work out how to connect the display to the RS-422/RS-485 adapter. After some trial and error I managed to 
