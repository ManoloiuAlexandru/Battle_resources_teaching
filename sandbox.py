# """
# Aveti 5 servere fiecare find reprezentat de 8 variable care reprezinta caracteristici ale serverlor.
# Obesrvatii care o sa fie in curs: cele 5 servere o sa fie reprezentate intr-un program de networking care simuleaza in
# timp real cum ar functiona o retea
#
# Cerinte:
# 1) Sa se modifice si sa se specifice ce variabile nu sunt scrise corect(nu respecta PEP8) ca si referinta serverul cu
# id=1 este scris corect
# 2) Creati al 6 lea server care sa aiba atributele pe care le au si celelalte servere
# 3) Daca as fi scris server_id_one==1 ce ar fi insemnat ?
# 4) Daca as fi scris server_id_one=1 apoi server_id_one=2 si tot asa pana la server_id_one=5 ce rezultat ar fi avut
# la final server_id_one ?
# 5) Daca as fi scris in loc de server_vendor_one="Dell" server_vendor_one='Dell' ar fi fost vreo diferenta ?
#
# """
#
# server_id_one = 1
# server_name_one = "CRAGOL_DARTOFUS"
# server_vendor_one = "Dell"
# server_ip_one = "102.23.44.101"
# server_support_type_one = "Platinum"
# server_os_one = "RHEL Atomic Host 7"
# server_status_one = "on"
# server_kernel_one = "2.19.3-3423.134.1.e43.x68_89"
# server_domain_one = "ING"
# ########################################################
#
# server_id_two = 2
# server_ne_two = "GHLTAPOLCZ"
# ser_vendor_two = "HPE"
# server_ip_two = "102.23.44.102"
# server_surt_type_two = "GOLD"
# server_os_two = "RHEL Server 8.1"
# serveatus_two = "off"
# serr_kernel_two = "3.6.6-1223.564.3.e13.x86_64"
# server_domain_two = "BRD"
# ########################################################
#
# serverthree = 3
# servername_three = "SSRTLDFGDCZ"
# server_venor_three = "Lenovo"
# server_ip_ree = "102.23.44.103"
# serversupport_type_three = "GOLD"
# server_os_three = "Debian 12.6"
# serverstatus_three = "on"
# server_kernelthree = "5.69.2-5621.184.9.e31.x64_32"
# server_domain_three = "UNICREDIT"
# ########################################################
#
#
# server_idfour = 4
# server_four = "SSERVERSL"
# server_vendor_four = "Lenovo"
# serveri_four = "102.23.44.104"
# server_support_type_four = "Silver"
# serveos_four = "RHEL 6"
# serveratus_four = "on"
# ser_kernel_four = "1.1.1-2343.4.2.e32.x32_32"
# server_domain_four = "RAIFFEISEN"
# ########################################################
#
# serverIdFive = 5
# serverNameFive = "VRLKSOPPL"
# server_venddor_five = "CISCO"
# server_ip_five = "102.23.44.105"
# server_supfport_type_five = "Bronze"
# server_os_ffive = "RHEL 9.4"
# servefr_statuss_five = "on"
# serssver_kernsels_five = "2.4.3-1413.54.1.e3.x86_89"
# server_domain_five = "BCR"
# ########################################################
import json
import os

import pandas as pd


class OCI:

    def __init__(self, name, ocid, region, tenancy, compartment, compartment_ocid, network_domain_name):
        self.name = name
        self.ocid = ocid
        self.region = region
        self.tenancy = tenancy
        self.compartment = compartment
        self.compartment_ocid = compartment_ocid
        self.network_domain_name = network_domain_name
        ocis.append(self)


hostnames = {}
ocis = []

df = pd.read_excel("Compute-List.xlsx")

for i in range(0, len(df.Tenancy)):
    oci = OCI(df["Compute Name"][i], df["Compute OCID"][i], df.Region[i], df.Tenancy[i], df.Compartment[i],
              df["Compartment OCID"][i], df["Newtork Domain Name"][i])
    if df["Compartment"][i] not in hostnames:
        hostnames[df["Compartment"][i]] = [oci]
    else:
        hostnames[df["Compartment"][i]].append(oci)

final_result = {"_meta": {"hostvars": {}}}
os.makedirs("compute_outputdir", exist_ok=True)
for oci in ocis:
    try:
        with open(f"compute_outputdir/{oci.name + '.' + oci.network_domain_name}.yml", "w") as file:
            file.write(
                f'instance_ocid: "{oci.ocid}"\ntenancy: "{oci.tenancy}"\nregion: "{oci.region}"')
    except Exception as e:
        print(oci.name, "problem", e)

final_result["all"] = {"children": ["ungrouped", "nodes"]}
with open("output compute.json", "w") as file:
    file.write(json.dumps(final_result))
