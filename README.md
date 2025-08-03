# EFT-Single-Player-Tarkov-Vortex-Extension
This is an Extension for the Vortex Modding platform Created by Nexus Mods that allows you to use Vortex to manage your Single Player Tarkov mods.

Please Pardon the mess, This is all new to me from the Developer side. <br/>
Also, this page assumes you know how to use Vortex Mod Manager, If there's enough demand, I will attach a guide to using it. <br/>
---
<details close>
<summary>Installing/Updating the extension </summary>
  <div align="left">
    Go to the "Extensions" List in the Vortex app <br/>   
    <img width="238" height="410" alt="image" src="https://github.com/user-attachments/assets/1415c11c-7e1a-411f-a295-4d017e8e7b37" /> <br/> <br/>
    Click on the button in the bottom right and select the zip file you downloaded, "EFT - Single Player Tarkov Vortex Extension vx.x.x". <br/> 
    <img width="1297" height="155" alt="image" src="https://github.com/user-attachments/assets/f973fea5-ee8e-45d0-a0e7-357024a621ae" /> <br/> <br/>  
    Restart Vortex, and Search the "Extensions" List, if you see it, it successfuly installed, If not, Repeat install and restart. (I do not know why Multiple install attempts is needed sometimes) <br/> 
    <img width="612" height="187" alt="image" src="https://github.com/user-attachments/assets/193c7021-bb59-4ee2-8862-dfe9097e0e09" /> <br/> <br/>
    Go to the "Games" tab <br/> 
    <img width="259" height="544" alt="image" src="https://github.com/user-attachments/assets/f871b75a-c84b-4b9c-9788-c9c68a31dc0b" /> <br/> <br/>
    Search for "Tarkov" <br/>
    <img width="330" height="195" alt="image" src="https://github.com/user-attachments/assets/51401b8b-102c-43c7-889b-ea5a358feaba" /> <br/> <br/>
    Click on it to Activate and it should ask you where you have SPT installed, (Where are SPT.Server.exe and SPT.Launcher located). <br/> <br/>
    Congrats! Vortex can now handle your mod installs as well as activating or deactivating mods. <br/> <br/>
    To see where Vortex is downloading and staging your mods, go to the "Settings" List and check the "Mods" and "Download" Tabs, you can also change the paths for both if you have somewhere else you'd rather mods be stored. <br/> 
    <img width="1027" height="587" alt="image" src="https://github.com/user-attachments/assets/01885f83-763a-4b93-ac4f-8cd88f4e87b6" /> <br/>
  </div>
</details>

---
 
<details close>
<summary>Supported Tools</summary>
  <div align="left">
    Vortex allows you to create shortcuts to tools that can easily be accessed from your Vortex dashboard <br/>
    <img width="1924" height="357" alt="image" src="https://github.com/user-attachments/assets/40fa8a1a-53cb-4951-ad9a-dea6848558bf" /> <br/>  <br/>
    Included in the extension is the "SPT Server" and "SPT Launcher" shortcut's as well as the foundation for other popular Mod tools. <br/> 
    1. Server Value Manager, https://hub.sp-tarkov.com/files/file/379-server-value-modifier-svm/ <br/> 
    2. Load Order Editor Drag'n'Drop, https://hub.sp-tarkov.com/files/file/1923-load-order-editor-drag-drop/ <br/> 
    3. LOE - Load Order Editor, https://hub.sp-tarkov.com/files/file/1082-loe-load-order-editor/ <br/> 
    4. Acid's Bot Placement System, https://hub.sp-tarkov.com/files/file/2782-abps-acid-s-bot-placement-system/ <br/> <br/>
    
   **You will still need to download and install any of the above mods you wish to use into their expected (default) locations, I merely laid the basic file structure and pointers so that Vortex will instantly recognize and populate the shortcuts. Yes, Installing them as Vortex mods is fine and in fact is preferred.**

  Note: If there is a tool you wish to see added to the list, Let me know and I can add it.
  </div>
</details>

---

<details close>
<summary>Installing Mods</summary>
    <div align="left">
Unfortunately, It is not a completely hands off endeavour if you want to take advantage of all the features of Vortex: Proper Deployment, Dependencies and the Variants systems. <br/> <br/>

On a basic level, We will need to make sure that the mod is packaged as Vortex expects. Let's use [Server Value Modifier](https://hub.sp-tarkov.com/files/file/379-server-value-modifier-svm/) as an example that requires manual intervention, Apologies for putting you on blast GhostFenixx xP.
<img width="769" height="55" alt="image" src="https://github.com/user-attachments/assets/0b448fd4-9ba4-4be6-b4da-7fc6624c25ac" /> <br/>

First, we will open the Archive to check if the top level of the archive contains "user" and/or "BepInEx" folders or other files that need to deployed into the root EFT install Folder. As you can see, SVM is packaged to be extracted into the user/mods folder. <br/>
<img width="525" height="117" alt="image" src="https://github.com/user-attachments/assets/a1857f8f-11a0-4f98-924b-c56ce7e008e7" />

In your workspace, Create a 'user' Folder, Go inside, Create a 'mods' Folder, Go inside and Extract SVM. <br/>
Go back 2 levels to your workspace area and package the 'user' folder into an archive, <br/>
The top level of the Archive is now 'user' and th emod has been moved 2 levels down into the 'mods' Folder. <br/>
<img width="436" height="77" alt="image" src="https://github.com/user-attachments/assets/dd044842-dc03-466a-a451-e76a37b4046a" />
<img width="516" height="76" alt="image" src="https://github.com/user-attachments/assets/e2e79007-3d25-43c5-bdb1-dc70c73b970f" />

And That's it! Use Vortex to install this mod and once you Activate it for your Profile and Deploy, you will see the SVM tool shortcut show up on your dashboard and in the Upper Left shortcuts menu.
  </div>
</details>

---

<details open>
<summary>Creating Dependencies, <sup> or Why I did all this work in the first place </sup> </summary>
  <div align="left">
Alright, Let's start making use of the powerful features of Vortex, Creating links between mods so that Vortex can keep track of which mods Require other mods, Must Load After (or Before), or Shouldn't be Deployed with each other (Incompatible with). <sup> To those familiar with Vortex, the Variants system isn't available at this time. </sup> <br/> <br/>
    
Let's use Everyone's favorite AI overhaul mod. [SAIN - Solarint's AI Modifications - Full AI Combat System Replacement](https://hub.sp-tarkov.com/files/file/1062-sain-solarint-s-ai-modifications-full-ai-combat-system-replacement/) <br/>
    As you can see, Sain requires both [BigBrain](https://hub.sp-tarkov.com/files/file/1219-bigbrain/) and [Waypoints](https://hub.sp-tarkov.com/files/file/1119-waypoints-expanded-navmesh/). <br/>
    <sup> Because Solarint and DrakiaXYZ are GOATs, you only need to make filename changes to prep them for Vortex handling. </sup> <br/>

**Important Note: Vortex handles mod relationships by reading the file name so it would benefit us to do some formating ahead of time.**

To begin with, I like to put a unique identifier of the mod inside tildes, (I also like to add brackets too, but those are purely an Aesthetic choice) as well as it's dependents inside parentheses like so, <br/>
<img width="340" height="28" alt="image" src="https://github.com/user-attachments/assets/526d050f-c70e-4fc3-9e19-ed332174a12a" />
    
After installing, use the dependency button to create links between SAIN, BigBrain, and Waypoints, (if you have other versions of SAIN, you can add "Conflicts With" Link). <br/>
    Example of telling Vortex that SAIN 4.1.3 should not be loaded with other verions of SAIN (More specifically, It should not be loaded with ANY other mod that uses \~SAIN\~ in its file name) <br/>
    <img width="689" height="392" alt="image" src="https://github.com/user-attachments/assets/e08c33e8-402a-4935-b3e8-c6bdfdd90aa5" /> <br/> <br/>
When finished, you should see something similar to this, Notice how the links are made using the Unique ID we set earlier? That means if the mod auther changes the file name (hopefully to make vortex integration easier xP), the link will still work just fine.
    <img width="2380" height="293" alt="image" src="https://github.com/user-attachments/assets/b2783934-c7b7-4ef8-8fd8-76f67bd5734a" /> <br/> <br/>
Generally, I make 2 connections between mods,  <br/>
1. "Requires": using the version match notation, (SAIN 4.1.3 requires at least Version 1.3.2 of Bigbrain) <br/>
    <img width="686" height="387" alt="image" src="https://github.com/user-attachments/assets/674b09ef-4773-4361-add8-aa5ed0cb3333" /> <br/> <br/>
2. "Must Deploy After": using any version notation, (SAIN 4.1.3 Must Deploy After ANY version of Bigbrain) <br/>
    <img width="688" height="386" alt="image" src="https://github.com/user-attachments/assets/4c1e0fb3-50e3-4179-ba12-8ba2f85d40ad" /> <br/> <br/>

A great thing about having Vortex handle Dependency like this is that not only will it flag a warning that "Hey, some mod dependencies are not fulfilled"  <br/>
    <img width="509" height="71" alt="image" src="https://github.com/user-attachments/assets/5e0b4832-5e07-4abe-92bb-a248f89d3314" /> <br/> <br/>
But it will also let you know that "Hey, The mod you enabled depends on other mods, do you want to enable those as well?" <br/>
    <img width="915" height="536" alt="image" src="https://github.com/user-attachments/assets/327d5988-1a13-49e8-9981-7e97b9f368c6" /> <br/> <br/>
The same for is true for the other direction, No longer using SAIN? Do you also want to diasble BigBrain and WAypoints now as well? (It even leaves them alone if something else you have enabled still requires them) <br/>
   <img width="916" height="535" alt="image" src="https://github.com/user-attachments/assets/26fe48d1-f097-4400-bd99-668da0d1859f" /> <br/>

  </div>
</details>

---
