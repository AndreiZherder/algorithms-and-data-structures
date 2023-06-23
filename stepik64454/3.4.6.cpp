#include <iostream>
#include <vector>

#define ll long long
#define LLONG_MAX 9223372036854775807ll

using namespace std;


int dnum(int i, int j, int m){
    return i - j + m - 1;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n, m;
    cin >> n >> m;

    vector <vector <ll>> a(n, vector <ll> (m));
    for (ll i = 0; i < n; i++) {
        for (ll j = 0; j < m; j++) {
            cin >> a[i][j];
        }
    }
    vector <vector <pair <ll,ll>>> prev(n, vector <pair <ll,ll>> (m, make_pair(0, 0)));
    vector <vector <ll>> row(n, {LLONG_MAX, 0, 0});
    vector <vector <ll>> col(m, {LLONG_MAX, 0, 0});
    vector <vector <ll>> diag(n + m - 1, {LLONG_MAX, 0, 0});
    row[0][0] = a[0][0];
    row[0][1] = 0;
    row[0][2] = 0;
    col[0][0] = a[0][0];
    col[0][1] = 0;
    col[0][2] = 0;
    diag[dnum(0, 0, m)][0] = a[0][0];
    diag[dnum(0, 0, m)][1] = 0;
    diag[dnum(0, 0, m)][2] = 0;
    ll cur = a[0][0];
    ll mn, mini, minj;
    for (int j = 1; j < m; j ++) {
        mn = row[0][0];
        mini = row[0][1];
        minj = row[0][2];
        cur = mn + a[0][j];
        prev[0][j] = make_pair(mini, minj);
        if (cur < mn) {
            row[0][0] = cur;
            row[0][1] = 0;
            row[0][2] = j;
        }
        col[j][0] = cur;
        col[j][1] = 0;
        col[j][2] = j;
        diag[dnum(0, j, m)][0] = cur;
        diag[dnum(0, j, m)][1] = 0;
        diag[dnum(0, j, m)][2] = j;
    }

    for (int i = 1; i < n; i ++) {
        mn = col[0][0];
        mini = col[0][1];
        minj = col[0][2];
        cur = mn + a[i][0];
        prev[i][0] = make_pair(mini, minj);
        if (cur < mn) {
            col[0][0] = cur;
            col[0][1] = i;
            col[0][2] = 0;
        }
        row[i][0] = cur;
        row[i][1] = i;
        row[i][2] = 0;
        diag[dnum(i, 0, m)][0] = cur;
        diag[dnum(i, 0, m)][1] = i;
        diag[dnum(i, 0, m)][2] = 0;
    }


    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            if (row[i][0] < col[j][0]) {
                if (row[i][0] < diag[dnum(i, j, m)][0]){
                    mn = row[i][0];
                    mini = row[i][1];
                    minj = row[i][2];
                } else {
                    mn = diag[dnum(i, j, m)][0];
                    mini = diag[dnum(i, j, m)][1];
                    minj = diag[dnum(i, j, m)][2];
                }
            } else {
                if (col[j][0] < diag[dnum(i, j, m)][0]){
                    mn = col[j][0];
                    mini = col[j][1];
                    minj = col[j][2];
                } else {
                    mn = diag[dnum(i, j, m)][0];
                    mini = diag[dnum(i, j, m)][1];
                    minj = diag[dnum(i, j, m)][2];
                }
            }
            cur = mn + a[i][j];
            prev[i][j] = make_pair(mini, minj);
            if (cur < row[i][0]) {
                row[i][0] = cur;
                row[i][1] = i;
                row[i][2] = j;
            }
            if (cur < col[j][0]) {
                col[j][0] = cur;
                col[j][1] = i;
                col[j][2] = j;
            }
            if (cur < diag[dnum(i, j, m)][0]) {
                diag[dnum(i, j, m)][0] = cur;
                diag[dnum(i, j, m)][1] = i;
                diag[dnum(i, j, m)][2] = j;
            }
        }
    }

    ll i = n - 1;
    ll j = m - 1;
    vector <pair <ll, ll>> ans;
    ans.emplace_back(i, j);

    while (i != 0 or j != 0){
        ll ni = prev[i][j].first;
        ll nj = prev[i][j].second;
        i = ni;
        j = nj;
        ans.emplace_back(i, j);
    }
    cout << cur << " " << ans.size() << "\n";
    for (auto p = ans.rbegin(); p != ans.rend(); p++){
        cout << p->first + 1 << " " << p->second + 1 << endl;
    }
    return 0;
}
