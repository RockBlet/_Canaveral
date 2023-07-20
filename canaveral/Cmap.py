import nmap3

#version_detect("nmmapper.com")
class Cmap:
    def version_detect(self, url):
        nmap = nmap3.Nmap()
        result = nmap.nmap_version_detection(url)
        answer_list: list = []
        isIp: bool = True

        for value in result:
            if isIp:
                answer_list.append(value)
                isIp = False

            answer_list.append(result[value])

        ip = answer_list[0]
        os = answer_list[1]
        runtime = answer_list[2]
        stats = answer_list[3]
        #tasks_result = answer_list[4]

        ports = os["ports"]
        mac = os["macaddress"]
        state = os["state"]
        osData = os["osmatch"]

        redirect = {
            "ip" : ip,
            "macaddress": mac,
            "state": state,
            "osData": osData,
            "runtime": runtime,
            "stats": stats,
        }

        return redirect, ports



    