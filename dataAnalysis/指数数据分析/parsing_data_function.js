function decrypt(t, e) {
    for (var n = t.split(""), i = e.split(""), a = {}, r = [], o = 0; o < n.length / 2; o++)
        a[n[o]] = n[n.length / 2 + o];
    for (var s = 0; s < e.length; s++)
        r.push(a[i[s]]);
    return r.join("")
}