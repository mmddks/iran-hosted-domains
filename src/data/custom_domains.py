custom_domains = {
    "proxy": [
        "animelist.ir",
        "gamepass.ir",
    ],
    "direct": [
        "arvancdn.com",
        "arvancdn.ir",
        "digikalacloud.com",
        "glorytoon.com",
        "ketaabonline.com",
        "ketab.io",
        "maryamsoft.com",
        "nassaab.com",
        "nassaabpro.com",
        "restfulsms.com",
        "snapp.taxi",
        "sut.ac.ir",
        "taaghchecdn.com",
        "taranevis.com",
        "timcheh.com",
        "turkeykala.com",
        "parspack.com",
        "pi.hole",
        "bankino.digital",
        "tourism-bank.com",
        "hamrahcard.net",
        "nextpay.org",
        "zoomg.ir",
        "aparatsport.com",
        "rozmusic.com",
        "blubank.sb24.ir",
        "farsgamerpay.com",
        "fgtal.com",
        "sedastore.com",
        "pay98.app",
        "salambaabaa.com",
        "mimfarsi.com",
        "wiiz.ir",
        "shad.ir",
        "targoman.ir",
        "nournews.ir",
        "farazdaily.com",
        "jamaran.news",
        "hammihanonline.ir",
        "farhikhtegandaily.com",
        "ecoiran.com",
        "ettelaatonline.com",
        "dolatebahar.ir",
        "irannewspaper.ir",
        "irandaily.ir",
        "wepod.ir",
        "abankapp.ir",
        "ivbb.ir",
        "rqb.ir",
        "eghtesaad24.ir",
        "khordad.news",
        "kishvandnews.ir",
        "wizardingcenter.com",
        "dementor.ir",
        "armanmeli.ir",
        "armandaily.ir",
        "taadolnewspaper.ir",
        "pishkhan.com",
        "ana.press",
        "tandisfood.ir",
        "azadfekrischool.ir",
        "azad.im",
        "bitbarg.com",
        "bitmit.co",
        "exbito.com",
        "arzpaya.com",
        "bittestan.com",
        "bitmax.ir",
        "erythron.net",
        "arvanstorage.com",
        "digijojeh.com",
        "masirwp.com",
        "microless.shop",
        "boomidi.net",
        "shab.cloud",
        "kermanmotor.com",
        "ticket-charter.com",
        "blitcharter.com",
        "digicharter.com",
        "kishzoom.net",
        "charter1.net",
        "charter361.com",
        "amincharter.com",
        "mancharter.net",
        "ba-charter.com",
        "charter724.vip",
        "cheapcharter.net",
        "kish44.com",
        "mlt.link",
        "iranianbirdingclub.com",
        "parsiday.com",
        "ostadpaz.com",
        "raykanet.com",
        "cafeartini.com",
        "ir.archive.ubuntu.com",
        "ir.prod.hosts.ooklaserver.net",
        "dadhotel.com",
        "adnetwork.credit",
        "shahrad.net",
        "khanesony.co",
        "danemarket.com",
        "openapi.sdb247.com",
        "tapsi.cab",
        "tap30.services,
"
    ],
    "remove": [
        "googleapis.com",
        "gvt1.com",
        "eset.com",
        "ubuntu.com",
        "radiojavan.com",
        "github.io",
        "wordpress.com",
    ],
    "remove_contain": [
        "google.com",
        "ooklaserver.net",
    ],
    "remove_regex": [
        r"^xn--",
    ],
}

if __name__ == "__main__":
    import json
    print(json.dumps(custom_domains))
