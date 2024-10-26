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
]


def is_adherent(name:str) -> bool:
    return name in NAMES_ADHERENTS


async def update(member):

    role_ADHERENT = member.guild.get_role(1252285875883348051)

    if not role_ADHERENT:
        return

    if is_adherent(member.global_name):
        if role_ADHERENT not in member.roles:
            await member.add_roles(role_ADHERENT)
    else:
        if role_ADHERENT in member.roles:
            await member.remove_roles(role_ADHERENT)