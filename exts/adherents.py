# coding : utf-8
# Python 3.10
# ----------------------------------------------------------------------------


NAMES_ADHERENTS = [
    "xelouuuuuu",
    "asurix_x",
    "Haruki0571",
    "michiland",
    "natzuzu",
    "estebanqgb",
    "thesurvivor64",
    "leira_de_lorea",
    "gwen157",
    "kureteiyu",
    "dramaqueenmrw",
    "mat_m_",
    "hubupper",
    "ishigami_fa_sol",
    "mano7ie.",
    "__susanoo",
    "toutoule_powpow",
    "nina.0410",
    "thefox580",
    "dabreton",
    "anthymefgn",
    "simp4koko",
    "emmyos__",
    "ShuriKeen3_37526",
    "oceanemuller",
    "Gwen157",
    "leira_de_lorea",
    "Toutoule_powpow",
    "Haokai",
    "_kekra_",
    "thesurvivor64",
    "xelouuu",
    "michiland",
    "r3draf",
    "mat_m_",
    "kureteiyu",
    "eva1812",
    "etandesdeschoses",
    "camillekst_",
    "c.clec",
    "danhheloise",
    "oceane.lcd",
    "gsuisnoa",
    "julpija",
    "dawadinho",
    "vikus_vie",
    "lomolosau",
]


def is_adherent(name:str) -> bool:
    return name.lower() in [n.lower() for n in NAMES_ADHERENTS]


async def update(member):

    role_ADHERENT = member.guild.get_role(1252285875883348051)

    if not role_ADHERENT:
        return

    if not member.name:
        return

    if is_adherent(member.name):
        if role_ADHERENT not in member.roles:
            await member.add_roles(role_ADHERENT)
    else:
        if role_ADHERENT in member.roles:
            await member.remove_roles(role_ADHERENT)
