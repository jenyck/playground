#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:64000000")
 
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <utility>
 
#include <set>
#include <map>
#include <vector>
#include <string>
#include <queue>
 
#include <iostream>
#include <sstream>
 
using namespace std;

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()

const int INF = (int)1E9;
const int64 INF64 = (int64)1E18;
const long double EPS = 1E-8;
const long double PI = 3.1415926535897932384626433832795;


int n, k, sum[20], need[20], ans[20];
string a[20], b[20];
map<string, int> m;
 
void init() {
    m["H"] = 1;
    m["He"] = 2;
    m["Li"] = 3;
    m["Be"] = 4;
    m["B"] = 5;
    m["C"] = 6;
    m["N"] = 7;
    m["O"] = 8;
    m["F"] = 9;
    m["Ne"] = 10;
    m["Na"] = 11;
    m["Mg"] = 12;
    m["Al"] = 13;
    m["Si"] = 14;
    m["P"] = 15;
    m["S"] = 16;
    m["Cl"] = 17;
    m["Ar"] = 18;
    m["K"] = 19;
    m["Ca"] = 20;
    m["Sc"] = 21;
    m["Ti"] = 22;
    m["V"] = 23;
    m["Cr"] = 24;
    m["Mn"] = 25;
    m["Fe"] = 26;
    m["Co"] = 27;
    m["Ni"] = 28;
    m["Cu"] = 29;
    m["Zn"] = 30;
    m["Ga"] = 31;
    m["Ge"] = 32;
    m["As"] = 33;
    m["Se"] = 34;
    m["Br"] = 35;
    m["Kr"] = 36;
    m["Rb"] = 37;
    m["Sr"] = 38;
    m["Y"] = 39;
    m["Zr"] = 40;
    m["Nb"] = 41;
    m["Mo"] = 42;
    m["Tc"] = 43;
    m["Ru"] = 44;
    m["Rh"] = 45;
    m["Pd"] = 46;
    m["Ag"] = 47;
    m["Cd"] = 48;
    m["In"] = 49;
    m["Sn"] = 50;
    m["Sb"] = 51;
    m["Te"] = 52;
    m["I"] = 53;
    m["Xe"] = 54;
    m["Cs"] = 55;
    m["Ba"] = 56;
    m["La"] = 57;
    m["Ce"] = 58;
    m["Pr"] = 59;
    m["Nd"] = 60;
    m["Pm"] = 61;
    m["Sm"] = 62;
    m["Eu"] = 63;
    m["Gd"] = 64;
    m["Tb"] = 65;
    m["Dy"] = 66;
    m["Ho"] = 67;
    m["Er"] = 68;
    m["Tm"] = 69;
    m["Yb"] = 70;
    m["Lu"] = 71;
    m["Hf"] = 72;
    m["Ta"] = 73;
    m["W"] = 74;
    m["Re"] = 75;
    m["Os"] = 76;
    m["Ir"] = 77;
    m["Pt"] = 78;
    m["Au"] = 79;
    m["Hg"] = 80;
    m["Tl"] = 81;
    m["Pb"] = 82;
    m["Bi"] = 83;
    m["Po"] = 84;
    m["At"] = 85;
    m["Rn"] = 86;
    m["Fr"] = 87;
    m["Ra"] = 88;
    m["Ac"] = 89;
    m["Th"] = 90;
    m["Pa"] = 91;
    m["U"] = 92;
    m["Np"] = 93;
    m["Pu"] = 94;
    m["Am"] = 95;
    m["Cm"] = 96;
    m["Bk"] = 97;
    m["Cf"] = 98;
    m["Es"] = 99;
    m["Fm"] = 100;
    m["Md"] = 101;
    m["No"] = 102;
    m["Lr"] = 103;
    m["Rf"] = 104;
    m["Db"] = 105;
}
 
void print(vector<int> t, string el) {
    forn(i, t.size()) {
        if (i != 0) cout << "+";
        cout << a[t[i]];
    }
    cout << "->" << el << endl;
}
 
void gen(int pos) {
    if (pos == n) {
        vector<int> res[20];
        forn(i, n) res[ans[i]].pb(i);
 
        cout << "YES" << endl;
        forn(i, k)
            print(res[i], b[i]);
 
        exit(0);
    }
 
    int w = m[a[pos]];
    forn(i, k)
        if (w + sum[i] <= need[i]) {
            sum[i] += w;
            ans[pos] = i;
            gen(pos + 1);
            sum[i] -= w;
        }
}
 
int main(){
#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    init();
    cin >> n >> k;
    forn(i, n) cin >> a[i];
    forn(i, k) cin >> b[i];
 
    forn(i, k)
        need[i] = m[b[i]];
 
    gen(0);
    cout << "NO" << endl;
 
    cerr << clock() * 1.0 / CLOCKS_PER_SEC << endl;
 
    return 0;
}