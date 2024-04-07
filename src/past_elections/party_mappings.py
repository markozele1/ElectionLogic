# for year in election_data.keys():
#     print("Year", year)
#     print("------------")
#     visited = []
#     for c in election_data[year].keys():
#         print("\tConstituency", c)
#         for party in election_data[year][c]:
#             if party.votes > 1000 and party.name not in visited:
#                 visited.append(party.name)
#                 print("\t\t-", party.name)


# for year in election_data.keys():
#     print("Year", year)
#     print("------------")
#     visited = []
#     for c in election_data[year].keys():
#         print("\tConstituency", c)
#         for party in election_data[year][c]:
#             if party.votes > 1000 and party.name not in visited:
#                 visited.append(party.name)
#                 print("\t\t-", party.name)


parties_mapping = {
    2015: {
        "SOCIJALDEMOKRATSKA PARTIJA HRVATSKE - SDP, HRVATSKA NARODNA STRANKA - LIBERALNI DEMOKRATI - HNS, HRVATSKA STRANKA UMIROVLJENIKA - HSU, HRVATSKI LABURISTI - STRANKA RADA, AUTOHTONA - HRVATSKA SELJAČKA STRANKA - A - HSS, ZAGORSKA STRANKA - ZS": "SDP",
        "HRVATSKA DEMOKRATSKA ZAJEDNICA - HDZ, HRVATSKA SELJAČKA STRANKA - HSS, HRVATSKA STRANKA PRAVA DR. ANTE STARČEVIĆ - HSP AS, BLOK UMIROVLJENICI ZAJEDNO - BUZ, HRVATSKA SOCIJALNO - LIBERALNA STRANKA - HSLS, HRAST - POKRET ZA USPJEŠNU HRVATSKU, HRVATSKA DEMOKRŠĆANSKA STRANKA - HDS, ZAGORSKA DEMOKRATSKA STRANKA - ZDS": "HDZ",
        "MOST NEZAVISNIH LISTA - MOST": "MOST",
        '"BANDIĆ MILAN 365 - STRANKA RADA I SOLIDARNOSTI", DEMOKRATSKA PRIGORSKO - ZAGREBAČKA STRANKA - DPS, DEMOKRATSKA STRANKA ŽENA - DSŽ, HRVATSKA EUROPSKA STRANKA - HES, HRVATSKA RADNIČKA STRANKA - HRS, HRVATSKA STRANKA ZELENIH - EKO SAVEZ - ZELENI, ISTARSKI DEMOKRATI - DEMOCRATICI ISTRIANI - ID - DI, MEĐIMURSKA STRANKA - MS, NEZAVISNI SELJACI HRVATSKE - NSH, NOVI VAL - STRANKA RAZVOJA - NOVI VAL, STRANKA UMIROVLJENIKA - SU, UMIROVLJENIČKA DEMOKRATSKA UNIJA - UDU, ZELENI SAVEZ - ZELENI, ZELENA STRANKA - ZS': "STRANKA RADA I SOLIDARNOSTI",
        "ODRŽIVI RAZVOJ HRVATSKE - ORaH": "ORaH",
        "U IME OBITELJI - PROJEKT DOMOVINA": "PROJEKT DOMOVINA",
        "NAPRIJED HRVATSKA! - PROGRESIVNI SAVEZ IVE JOSIPOVIĆA, NARODNA STRANKA - REFORMISTI - REFORMISTI, STRANKA HRVATSKIH UMIROVLJENIKA - UMIROVLJENICI, ZELENI FORUM, DUBROVAČKI DEMOKRATSKI SABOR - DDS": "NAPRIJED HRVATSKA!, REFORMISTI",
        "NARODNA STRANKA - REFORMISTI - REFORMISTI, NAPRIJED HRVATSKA! - PROGRESIVNI SAVEZ IVE JOSIPOVIĆA, STRANKA HRVATSKIH UMIROVLJENIKA - UMIROVLJENICI, ZELENI FORUM, DUBROVAČKI DEMOKRATSKI SABOR - DDS": "NAPRIJED HRVATSKA!, REFORMISTI",
        "AUTOHTONA - HRVATSKA STRANKA PRAVA - A - HSP": "A-HSP",
        "HRVATSKI DEMOKRATSKI SAVEZ SLAVONIJE I BARANJE - HDSSB": "HDSSB",
        "DEMOKRATSKI SAVEZ NACIONALNE OBNOVE - DESNO": "DESNO",
        "HRVATSKA KONZERVATIVNA STRANKA - HKS, HRVATSKA STRANKA PRAVA - HSP, OBITELJSKA STRANKA - OS": "HKS, HSP",
        "ISTARSKI DEMOKRATSKI SABOR - IDS, PRIMORSKO GORANSKI SAVEZ - PGS, LISTA ZA RIJEKU - RI": "IDS",
        'BANDIĆ MILAN 365 - STRANKA RADA I SOLIDARNOSTI", ISTARSKI DEMOKRATI - DEMOCRATICI ISTRIANI - ID - DI, DEMOKRATSKA PRIGORSKO - ZAGREBAČKA STRANKA - DPS, DEMOKRATSKA STRANKA ŽENA - DSŽ, HRVATSKA EUROPSKA STRANKA - HES, HRVATSKA RADNIČKA STRANKA - HRS, HRVATSKA STRANKA ZELENIH - EKO SAVEZ - ZELENI, MEĐIMURSKA STRANKA - MS, NEZAVISNI SELJACI HRVATSKE - NSH, NOVI VAL - STRANKA RAZVOJA - NOVI VAL, STRANKA UMIROVLJENIKA - SU, UMIROVLJENIČKA DEMOKRATSKA UNIJA - UDU, ZELENI SAVEZ - ZELENI, ZELENA STRANKA - ZS': "STRANKA RADA I SOLIDARNOSTI",
        "AKCIJA MLADIH - AM": "AM",
        "SOCIJALDEMOKRATSKA PARTIJA HRVATSKE - SDP, HRVATSKA NARODNA STRANKA - LIBERALNI DEMOKRATI - HNS, HRVATSKA STRANKA UMIROVLJENIKA - HSU, HRVATSKI LABURISTI - STRANKA RADA, AUTOHTONA - HRVATSKA SELJAČKA STRANKA - A - HSS, ZAGORSKA STRANKA - ZS, SAMOSTALNA DEMOKRATSKA SRPSKA STRANKA - SDSS": "SDP",
        "ŽIVI ZID, AKCIJA MLADIH - AM": "ŽIVI ZID",
        "HRVATSKA ZORA STRANKA NARODA - HZ": "HZ",
        "HRVATSKA DEMOKRATSKA ZAJEDNICA - HDZ, HRVATSKA SELJAČKA STRANKA - HSS, HRVATSKA STRANKA PRAVA DR. ANTE STARČEVIĆ - HSP AS, BLOK UMIROVLJENICI ZAJEDNO - BUZ, HRVATSKA SOCIJALNO - LIBERALNA STRANKA - HSLS, HRVATSKA DEMOKRŠĆANSKA STRANKA - HDS, ZAGORSKA DEMOKRATSKA STRANKA - ZDS, HRAST - POKRET ZA USPJEŠNU HRVATSKU": "HDZ",
        "NARODNA STRANKA - REFORMISTI - REFORMISTI, DUBROVAČKI DEMOKRATSKI SABOR - DDS, NAPRIJED HRVATSKA! - PROGRESIVNI SAVEZ IVE JOSIPOVIĆA, STRANKA HRVATSKIH UMIROVLJENIKA - UMIROVLJENICI, ZELENI FORUM": "NAPRIJED HRVATSKA!, REFORMISTI",
        "BRANITELJSKO DOMOLJUBNA STRANKA HRVATSKE - BDSH, HRVATSKA BRANITELJSKA PUČKA STRANKA - HBPS": "HBPS",
        "BRANITELJSKO DOMOLJUBNA STRANKA HRVATSKE - BDSH": "BDSH",
        '"BANDIĆ MILAN 365 - STRANKA RADA I SOLIDARNOSTI", ISTARSKI DEMOKRATI - DEMOCRATICI ISTRIANI - ID - DI, DEMOKRATSKA PRIGORSKO - ZAGREBAČKA STRANKA - DPS, DEMOKRATSKA STRANKA ŽENA - DSŽ, HRVATSKA EUROPSKA STRANKA - HES, HRVATSKA RADNIČKA STRANKA - HRS, HRVATSKA STRANKA ZELENIH - EKO SAVEZ - ZELENI, MEĐIMURSKA STRANKA - MS, NEZAVISNI SELJACI HRVATSKE - NSH, NOVI VAL - STRANKA RAZVOJA - NOVI VAL, STRANKA UMIROVLJENIKA - SU, UMIROVLJENIČKA DEMOKRATSKA UNIJA - UDU, ZELENI SAVEZ - ZELENI, ZELENA STRANKA - ZS': "STRANKA RADA I SOLIDARNOSTI"
    },
    2016: {
        "SOCIJALDEMOKRATSKA PARTIJA HRVATSKE - SDP, HRVATSKA NARODNA STRANKA - LIBERALNI DEMOKRATI - HNS, HRVATSKA SELJAČKA STRANKA - HSS, HRVATSKA STRANKA UMIROVLJENIKA - HSU": "SDP",
        "HRVATSKA DEMOKRATSKA ZAJEDNICA - HDZ, HRVATSKA SOCIJALNO - LIBERALNA STRANKA - HSLS": "HDZ",
        "MOST NEZAVISNIH LISTA - MOST": "MOST",
        "ŽIVI ZID, PROMIJENIMO HRVATSKU, AKCIJA MLADIH, ABECEDA DEMOKRACIJE": "ŽIVI ZID",
        "PAMETNO, ZA GRAD": "PAMETNO",
        '"BANDIĆ MILAN 365 - STRANKA RADA I SOLIDARNOSTI" - "STRANKA RADA I SOLIDARNOSTI", NARODNA STRANKA - REFORMISTI - REFORMISTI, NOVI VAL - STRANKA RAZVOJA - NOVI VAL, HRVATSKA SELJAČKA STRANKA - STJEPAN RADIĆ - HSS - SR, BLOK UMIROVLJENICI ZAJEDNO - BUZ': "STRANKA RADA I SOLIDARNOSTI",
        "SASVIM MALA STRANKA - SMS": "SMS",
        "ŽIVI ZID, PROMIJENIMO HRVATSKU, AKCIJA MLADIH, HRVATSKA DEMOKRATSKA SELJAČKA STRANKA, ABECEDA DEMOKRACIJE": "ŽIVI ZID",
        "STRANKA UMIROVLJENIKA - SU": "SU",
        "HRVATSKA STRANKA PRAVA - HSP, HRVATSKA ČISTA STRANKA PRAVA - HČSP, AKCIJA ZA BOLJU HRVATSKU - ABH, OBITELJSKA STRANKA - OS": "HSP",
        "HRVATSKA DEMOKRATSKA ZAJEDNICA - HDZ": "HDZ",
        "ŽIVI ZID, PROMIJENIMO HRVATSKU, AKCIJA MLADIH, ABECEDA DEMOKRACIJE, HRVATSKA DEMOKRATSKA SELJAČKA STRANKA, MEĐIMURSKA STRANKA": "ŽIVI ZID",
        "NEZAVISNA LISTA STIPE PETRINA - NLSP, SLOBODNA HRVATSKA - SH, POKRET ZAJEDNO, ODRŽIVI RAZVOJ HRVATSKE - ORaH": "ORaH",
        "HRVATSKI LABURISTI - STRANKA RADA - LABURISTI": "LABURISTI",
        "HRVATSKI DEMOKRATSKI SAVEZ SLAVONIJE I BARANJE - HDSSB, HRVATSKA KONZERVATIVNA STRANKA - HKS": "HDSSB",
        "HRVATSKA STRANKA PRAVA DR. ANTE STARČEVIĆ - HSP AS, DEMOKRATSKI SAVEZ NACIONALNE OBNOVE - DESNO, HRVATSKA KRŠĆANSKA DEMOKRATSKA UNIJA - DR. MARKO VESELICA - HKDU - DR. MARKO VESELICA, HRVATSKA DEMOKRATSKA STRANKA - HDS, UJEDINJENA STRANKA PRAVA - USP": "HSP",
        "ŽIVI ZID, PROMIJENIMO HRVATSKU, AKCIJA MLADIH": "ŽIVI ZID",
        "HRVATSKA STRANKA PRAVA DR. ANTE STARČEVIĆ - HSP AS, DEMOKRATSKI SAVEZ NACIONALNE OBNOVE - DESNO, HRVATSKA KRŠĆANSKA DEMOKRATSKA UNIJA - DR. MARKO VESELICA - HKDU - DR. MARKO VESELICA, UJEDINJENA STRANKA PRAVA - USP, HRVATSKA DEMOKRATSKA STRANKA - HDS": "HSP",
        "HRVATSKA STRANKA PRAVA DR. ANTE STARČEVIĆ - HSP AS, HRVATSKA KRŠĆANSKA DEMOKRATSKA UNIJA - DR. MARKO VESELICA - HKDU - DR. MARKO ": "HSP",
        "PRIMORSKO GORANSKI SAVEZ - PGS, ISTARSKI DEMOKRATSKI SABOR - IDS, LISTA ZA RIJEKU - RI": "IDS",
        "ISTARSKI DEMOKRATSKI SABOR - IDS, PRIMORSKO GORANSKI SAVEZ - PGS, LISTA ZA RIJEKU - RI": "IDS",
        "ISTARSKI DEMOKRATI - DEMOCRATICI ISTRIANI - ID - DI": "ID",
        "NEZAVISNA LISTA STIPE PETRINA - NLSP, SLOBODNA HRVATSKA - SH, POKRET ZAJEDNO, ODRŽIVI RAZVOJ HRVATSKE - ORaH, STRANKA HRVATSKOG ZAJEDNIŠTVA - SHZ, STRANKA UMIROVLJENIKA - SU": "ORaH",
        "HRVATSKA DEMOKRATSKA ZAJEDNICA - HDZ, HRVATSKA DEMOKRŠĆANSKA STRANKA - HDS": "HDZ",
        "EZAVISNA LISTA STIPE PETRINA - NLSP, SLOBODNA HRVATSKA - SH, POKRET ZAJEDNO, ODRŽIVI RAZVOJ HRVATSKE - ORaH, STRANKA UMIROVLJENIKA - SU": "ORaH",
        "BRANITELJSKO DOMOLJUBNA STRANKA HRVATSKE - BDSH, HRVATSKA BRANITELJSKA PUČKA STRANKA - HBPS": "HBPS",
        "BRANITELJSKO DOMOLJUBNA STRANKA HRVATSKE - BDSH": "BDSH",
        "AUTOHTONA - HRVATSKA STRANKA PRAVA - A - HSP": "A-HSP",
        '"BANDIĆ MILAN 365 - STRANKA RADA I SOLIDARNOSTI", ISTARSKI DEMOKRATI - DEMOCRATICI ISTRIANI - ID - DI, DEMOKRATSKA PRIGORSKO - ZAGREBAČKA STRANKA - DPS, DEMOKRATSKA STRANKA ŽENA - DSŽ, HRVATSKA EUROPSKA STRANKA - HES, HRVATSKA RADNIČKA STRANKA - HRS, HRVATSKA STRANKA ZELENIH - EKO SAVEZ - ZELENI, MEĐIMURSKA STRANKA - MS, NEZAVISNI SELJACI HRVATSKE - NSH, NOVI VAL - STRANKA RAZVOJA - NOVI VAL, STRANKA UMIROVLJENIKA - SU, UMIROVLJENIČKA DEMOKRATSKA UNIJA - UDU, ZELENI SAVEZ - ZELENI, ZELENA STRANKA - ZS': "STRANKA RADA I SOLIDARNOSTI"
    },
    2020: {
        "HRVATSKA DEMOKRATSKA ZAJEDNICA - HDZ, HRVATSKA SOCIJALNO - LIBERALNA STRANKA - HSLS": "HDZ",
        "SOCIJALDEMOKRATSKA PARTIJA HRVATSKE - SDP, HRVATSKA SELJAČKA STRANKA - HSS, HRVATSKA STRANKA UMIROVLJENIKA - HSU, SNAGA - STRANKA NARODNOG I GRAĐANSKOG AKTIVIZMA - SNAGA, GRAĐANSKO-LIBERALNI SAVEZ - GLAS, ISTARSKI DEMOKRATSKI SABOR - IDS, PRIMORSKO GORANSKI SAVEZ - PGS": "SDP",
        "MOŽEMO! - POLITIČKA PLATFORMA, ZAGREB JE NAŠ!, NOVA LJEVICA - NL, RADNIČKA FRONTA - RF, ODRŽIVI RAZVOJ HRVATSKE - ORAH, ZA GRAD": "MOŽEMO!",
        "DOMOVINSKI POKRET MIROSLAVA ŠKORE - DOMOVINSKI POKRET, HRVATSKI SUVERENISTI, BLOK ZA HRVATSKU - BLOK, HRVATSKA KONZERVATIVNA STRANKA - HKS, HRAST - POKRET ZA USPJEŠNU HRVATSKU, STRANKA UMIROVLJENIKA - SU, ZELENA LISTA": "DOMOVINSKI POKRET",
        "MOST NEZAVISNIH LISTA - MOST": "MOST",
        "STRANKA S IMENOM I PREZIMENOM, PAMETNO, FOKUS": "PAMETNO",
        "ŽIVI ZID, PROMIJENIMO HRVATSKU - PH, HRVATSKA SELJAČKA STRANKA - STJEPAN RADIĆ - HSS - SR, STRANKA IVANA PERNARA - SIP, HRVATSKA STRANKA SVIH ČAKAVACA KAJKAVACA I ŠTOKAVACA - HSSČKŠ, ZAGORSKA STRANKA ZA ZAGREB - ZSZ, NEZAVISNA LISTA STIPE PETRINA - NLSP": "ŽIVI ZID",
        '"BANDIĆ MILAN 365 - STRANKA RADA I SOLIDARNOSTI" - "365 STRANKA RADA I SOLIDARNOSTI"': "STRANKA RADA I SOLIDARNOSTI",
        "ŽELJKO LACKOVIĆ - NEZAVISNE LISTE, NARODNA STRANKA - REFORMISTI - REFORMISTI, HRVATSKA SELJAČKA STRANKA BRAĆE RADIĆ - HSS BRAĆE RADIĆ, NEZAVISNI SELJACI HRVATSKE - NSH, HRVATSKA DEMOKRŠĆANSKA STRANKA - HDS": "REFORMISTI",
        "HRVATSKA DEMOKRATSKA ZAJEDNICA - HDZ": "HDZ",
        "HRVATSKA NARODNA STRANKA - LIBERALNI DEMOKRATI - HNS": "HNS",
        "NARODNA STRANKA - REFORMISTI - REFORMISTI, HRVATSKA SELJAČKA STRANKA BRAĆE RADIĆ - HSS BRAĆE RADIĆ, STRANKA HRVATSKIH UMIROVLJENIKA - UMIROVLJENICI - UMIROVLJENICI": "REFORMISTI",
        "MOŽEMO! - POLITIČKA PLATFORMA, NOVA LJEVICA - NL, RADNIČKA FRONTA - RF, ODRŽIVI RAZVOJ HRVATSKE - ORAH, ZAGREB JE NAŠ!, ZA GRAD": "MOŽEMO!",
        "HRVATSKA NARODNA STRANKA - LIBERALNI DEMOKRATI - HNS, HRVATSKA SELJAČKA STRANKA BRAĆE RADIĆ - HSS BRAĆE RADIĆ": "HNS",
        "SNAGA SLAVONIJE I BARANJE - Snaga SiB": "Snaga SiB",
        "SOCIJALDEMOKRATSKA PARTIJA HRVATSKE - SDP, HRVATSKA SELJAČKA STRANKA - HSS, HRVATSKA STRANKA UMIROVLJENIKA - HSU, SNAGA - STRANKA NARODNOG I GRAĐANSKOG AKTIVIZMA - SNAGA, GRAĐANSKO-LIBERALNI SAVEZ - GLAS, ISTARSKI DEMOKRATSKI SABOR - IDS, PRIMORSKO GORANSKI SAVEZ - PGS, NARODNA STRANKA - REFORMISTI - REFORMISTI": "SDP",
        "SOCIJALDEMOKRATSKA PARTIJA HRVATSKE - SDP, ISTARSKI DEMOKRATSKI SABOR - IDS, PRIMORSKO GORANSKI SAVEZ - PGS, HRVATSKA SELJAČKA STRANKA - HSS, HRVATSKA STRANKA UMIROVLJENIKA - HSU, SNAGA - STRANKA NARODNOG I GRAĐANSKOG AKTIVIZMA - SNAGA, GRAĐANSKO-LIBERALNI SAVEZ - GLAS": "SDP",
        "MOŽEMO! - POLITIČKA PLATFORMA, RADNIČKA FRONTA - RF, NOVA LJEVICA - NL, ODRŽIVI RAZVOJ HRVATSKE - ORAH, ZAGREB JE NAŠ!, ZA GRAD": "MOŽEMO!",
        "DEMOKRATI, HRVATSKI LABURISTI - STRANKA RADA, LISTA ZA RIJEKU": "LABURISTI",
        "UNIJA KVARNERA - UNIJA": "UNIJA",
        "NEZAVISNA LISTA STIPE PETRINA - NLSP, AKCIJA MLADIH - AM, ŽIVI ZID, PROMIJENIMO HRVATSKU - PH, STRANKA IVANA PERNARA - SIP": "ŽIVI ZID",
        "NEOVISNI ZA HRVATSKU - NHR, HRVATSKA STRANKA PRAVA - HSP, GENERACIJA OBNOVE - GO": "HSP",
        "HRVATSKA DEMOKRATSKA ZAJEDNICA - HDZ, HRVATSKA DEMOKRŠĆANSKA STRANKA - HDS": "HDZ",
        "BRANITELJSKO DOMOLJUBNA STRANKA HRVATSKE - BDSH, HRVATSKA BRANITELJSKA PUČKA STRANKA - HBPS": "HBPS",
        "BRANITELJSKO DOMOLJUBNA STRANKA HRVATSKE - BDSH": "BDSH",
        "AUTOHTONA - HRVATSKA STRANKA PRAVA - A - HSP": "A-HSP",
        '"BANDIĆ MILAN 365 - STRANKA RADA I SOLIDARNOSTI", ISTARSKI DEMOKRATI - DEMOCRATICI ISTRIANI - ID - DI, DEMOKRATSKA PRIGORSKO - ZAGREBAČKA STRANKA - DPS, DEMOKRATSKA STRANKA ŽENA - DSŽ, HRVATSKA EUROPSKA STRANKA - HES, HRVATSKA RADNIČKA STRANKA - HRS, HRVATSKA STRANKA ZELENIH - EKO SAVEZ - ZELENI, MEĐIMURSKA STRANKA - MS, NEZAVISNI SELJACI HRVATSKE - NSH, NOVI VAL - STRANKA RAZVOJA - NOVI VAL, STRANKA UMIROVLJENIKA - SU, UMIROVLJENIČKA DEMOKRATSKA UNIJA - UDU, ZELENI SAVEZ - ZELENI, ZELENA STRANKA - ZS': "STRANKA RADA I SOLIDARNOSTI"
    }
}


def get_full_name(year, name):
    for p in parties_mapping[year]:
        if parties_mapping[year][p] == name:
            return p
    return name