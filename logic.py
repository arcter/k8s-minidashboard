
def get_links_for_ns(nc,ns):
    links=[]
    items=nc.list_namespaced_ingress(ns).items
    for item in items:
        for rule in item.spec.rules:
            for path in rule.http.paths:
                links.append("https://"+rule.host+path.path)
    return links

def get_links(nc):
    links=[]
    items=nc.list_ingress_for_all_namespaces().items
    for item in items:
        for rule in item.spec.rules:
            for path in rule.http.paths:
                links.append("https://"+rule.host+path.path)
    return links