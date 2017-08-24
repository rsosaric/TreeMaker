import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/641/00000/A27C6993-3A66-E711-A67D-02163E01A409.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/678/00000/D4B883E8-A766-E711-A280-02163E01A250.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/679/00000/8AA749BA-A766-E711-996D-02163E011F99.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/681/00000/1CFC386A-AE66-E711-9B6F-02163E0138C0.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/831/00000/5AA3596D-D667-E711-9AB8-02163E01A6DA.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/853/00000/3269F439-9968-E711-9C3A-02163E0124B2.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/853/00000/A442D221-A168-E711-B6CB-02163E0144F7.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/853/00000/BC8590B1-3D69-E711-8ECF-02163E013960.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/853/00000/BCC5D8FE-AE68-E711-A7C5-02163E01A4F8.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/853/00000/D02E31F6-C868-E711-92BF-02163E019E03.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/854/00000/6ABB9712-8468-E711-82E7-02163E014626.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/855/00000/FE224254-A168-E711-A432-02163E01A6C1.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/906/00000/54FF1DA5-B068-E711-B34C-02163E01398C.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/996/00000/82F01A1E-1F6A-E711-A259-02163E01A505.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/996/00000/9437F7BF-2E6A-E711-B591-02163E01A3B1.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/996/00000/A0919B33-516A-E711-9C48-02163E01398F.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/996/00000/DA990A84-186A-E711-AEE8-02163E011EE8.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/997/00000/5CEB5F34-1C6A-E711-8067-02163E01A5DC.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/298/998/00000/B627DF64-126A-E711-A735-02163E01A45A.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/000/00000/6AD56311-396A-E711-B18F-02163E01419D.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/000/00000/AE7BA3D8-2E6A-E711-8200-02163E011B5B.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/042/00000/4240272D-806A-E711-9BED-02163E011C04.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/061/00000/027ECA80-5D6B-E711-AAB7-02163E01A627.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/061/00000/149F8756-C06A-E711-910F-02163E013664.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/061/00000/242592D1-BD6A-E711-957C-02163E01A6D4.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/061/00000/32340617-BA6A-E711-A835-02163E011BDA.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/061/00000/481F71FB-AF6A-E711-B91A-02163E0143F9.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/061/00000/8CC21342-C66A-E711-9655-02163E019CAF.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/061/00000/90B3EDF4-B76A-E711-AA85-02163E01A5D4.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/061/00000/D24F4F27-B46A-E711-A4F3-02163E0146C2.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/062/00000/1A2D8769-C46A-E711-99A3-02163E01A2CE.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/062/00000/60768844-C76A-E711-8E5D-02163E0135F2.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/062/00000/6C025664-E76A-E711-B282-02163E019CE6.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/062/00000/6C9B3CF7-CA6A-E711-8CDA-02163E011F3F.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/062/00000/90C8917B-BE6A-E711-9E05-02163E012457.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/062/00000/9C96809B-C16A-E711-9009-02163E019E8E.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/062/00000/F42B8E25-CE6A-E711-B1B2-02163E0142C8.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/064/00000/70419C78-CC6A-E711-9028-02163E019C43.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/064/00000/DEE8F77E-E16A-E711-9133-02163E0135EF.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/065/00000/0A736827-FE6A-E711-90E1-02163E01A1FC.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/065/00000/0C233C1F-D66A-E711-8FC1-02163E011C13.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/065/00000/268235CC-D96A-E711-8BD9-02163E013960.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/065/00000/42EB0908-E06A-E711-86CA-02163E01412A.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/065/00000/5CD91745-DD6A-E711-9BCB-02163E014686.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/065/00000/68640E10-E46A-E711-833F-02163E01A70B.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/067/00000/16C26481-016B-E711-8E48-02163E01413A.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/067/00000/20DBA0B5-866B-E711-8F0F-02163E0136AF.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/067/00000/4AD5B04A-FA6A-E711-8731-02163E01A373.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/067/00000/C2725753-F46A-E711-ABED-02163E011DDE.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/067/00000/C8EDC034-F66A-E711-9BFD-02163E019BE1.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/067/00000/D0166036-F26A-E711-84A9-02163E011DD8.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/067/00000/E67CB3FB-EE6A-E711-B697-02163E011EE8.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/096/00000/0A9BFF33-236B-E711-A72A-02163E011F37.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/096/00000/A60DE2ED-316B-E711-8A03-02163E01A414.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/096/00000/A62EBEB4-1D6B-E711-A7E3-02163E011F05.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/0E4F7480-906B-E711-9C6D-02163E013558.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/46E0CFD9-996B-E711-9E37-02163E014106.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/6A4F47D7-966B-E711-9AB0-02163E01A5BB.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/72A8950D-896B-E711-A402-02163E011C1F.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/7A73BFC4-8E6B-E711-BC5C-02163E0136DA.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/8C29353E-AA6B-E711-A0F2-02163E01A6B4.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/B22EA15A-9C6B-E711-9145-02163E01A450.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/BC889561-926B-E711-BF4D-02163E01A709.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/C8E65E5C-8C6B-E711-BEBC-02163E01469A.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/F48F93DA-AE6B-E711-AEB3-02163E011F68.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/149/00000/FEA53FE3-936B-E711-986D-02163E01A57E.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/178/00000/10148829-E46B-E711-A836-02163E014127.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/178/00000/26B93B6C-FB6B-E711-A74E-02163E01A45A.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/180/00000/4A96909D-F66B-E711-AFDB-02163E0144F4.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/180/00000/54D99E08-E06B-E711-97CF-02163E01A61E.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/184/00000/0436130E-FA6B-E711-8BB9-02163E0143F9.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/184/00000/066841BE-FB6B-E711-A442-02163E01A6DD.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/184/00000/10B8C2E0-1B6C-E711-8102-02163E011D43.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/184/00000/203C4DAC-096C-E711-9719-02163E019B95.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/184/00000/2EE7B248-086C-E711-B404-02163E01A4AC.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/184/00000/44031ACE-0C6C-E711-9EAB-02163E01A314.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/184/00000/548EAC65-F26B-E711-BEB5-02163E011E1F.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/184/00000/6EF78D23-FD6B-E711-A6B5-02163E01A256.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/184/00000/9E25A2B1-F76B-E711-BF2E-02163E0141D8.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/184/00000/CE7CDAFC-006C-E711-A965-02163E0137FF.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/184/00000/DAACB53C-046C-E711-990C-02163E019C9A.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/184/00000/EC6AF23A-FE6B-E711-AA31-02163E014307.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/184/00000/F2283CFD-056C-E711-A05C-02163E014626.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/185/00000/70AFC755-0E6C-E711-A9CC-02163E019B4E.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/185/00000/B8D3A7F1-076C-E711-BBA3-02163E01A348.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/185/00000/D4C87DC4-026C-E711-A34B-02163E019B50.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/316/00000/C64508FF-6D6D-E711-B5F8-02163E019BE7.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/316/00000/FC0C78B7-616D-E711-A15F-02163E011DBE.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/317/00000/76671888-306D-E711-9F52-02163E019B62.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/318/00000/C44476BF-2E6D-E711-8B7E-02163E01A6D5.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/318/00000/E4775348-436D-E711-93E4-02163E01A2B7.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/324/00000/2221C56C-E86D-E711-9A41-02163E01A66B.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/324/00000/70CED465-166E-E711-8C04-02163E014265.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/325/00000/441380D1-326D-E711-8D4F-02163E011F04.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/325/00000/626BBF10-396D-E711-8C1D-02163E012A49.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/325/00000/80C5A517-3D6D-E711-95F3-02163E01A224.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/325/00000/A8AEA8AC-346D-E711-98E7-02163E0144D8.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/325/00000/D61861B9-776D-E711-BA25-02163E01441A.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/326/00000/18966B16-8D6D-E711-99E6-02163E013940.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/327/00000/264DBB4E-366D-E711-8173-02163E01A20A.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/327/00000/26EAD73A-406D-E711-910F-02163E0135A0.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/329/00000/96F691BB-4C6D-E711-80B7-02163E0119D7.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/329/00000/AE3D97BC-736D-E711-AEC7-02163E014235.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/329/00000/DE95050F-496D-E711-AA9C-02163E0144DD.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/329/00000/E42B4A9D-616D-E711-8687-02163E019D26.root',
'/store/data/Run2017B/JetHT/MINIAOD/PromptReco-v2/000/299/329/00000/FEDB1C68-456D-E711-92B2-02163E011FC2.root' ] );