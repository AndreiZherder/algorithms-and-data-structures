#include <iostream>
#include <vector>
#include <set>
#include <deque>

using namespace std;


int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n, m;
    cin >> n >> m;
    n = 2 * n + 1;
    m = 2 * m + 1;
    vector <string> grid;
    string s;
    getline(cin, s);
    for (int i = 0; i < n; i++){
        getline(cin, s);
        grid.push_back(s);
    }
    set <pair<int, int>> d;

    pair<int, int> start;
    for (int i = 1; i < n; i += 2) {
        for (int j = 1; j < m; j += 2) {
            if (grid[i][j] == 'S') {
                start = make_pair(i, j);
            }
            if (grid[i][j] == 'D') {
                d.emplace(i, j);
            }
        }
    }
    vector <vector <int>> seen(n, vector <int> (m));
    seen[start.first][start.second] = 1;
    deque <pair <int, int>> q;
    q.emplace_back(start);
    while (!q.empty()) {
        pair <int, int> cur = q[0];
        int i = cur.first;
        int j = cur.second;
        q.pop_front();
        if (grid[i - 1][j] == '-'){
            for (int ni = i + 2; ni < n; ni += 2){
                if (grid[ni - 1][j] == '-'){
                    break;
                }
                else{
                    if (not seen[ni][j]) {
                        if (grid[ni][j] == 'D') {
                            d.erase(make_pair(ni, j));
                        }
                        seen[ni][j] = 1;
                        if (grid[ni][j - 1] == '|' or grid[ni][j + 1] == '|') {
                            q.emplace_back(ni, j);
                        }
                    }
                    else if (seen[ni][j] & 1) {
                        break;
                    }
                    else{
                        seen[ni][j] |= 1;
                    }
                }
            }
        }

        if (grid[i + 1][j] == '-'){
            for (int ni = i - 2; ni > 0; ni -= 2){
                if (grid[ni + 1][j] == '-'){
                    break;
                }
                else{
                    if (not seen[ni][j]) {
                        if (grid[ni][j] == 'D') {
                            d.erase(make_pair(ni, j));
                        }
                        seen[ni][j] = 1;
                        if (grid[ni][j - 1] == '|' or grid[ni][j + 1] == '|') {
                            q.emplace_back(ni, j);
                        }
                    }
                    else if (seen[ni][j] & 1) {
                        break;
                    }
                    else{
                        seen[ni][j] |= 1;
                    }
                }
            }
        }
        if (grid[i][j - 1] == '|'){
            for (int nj = j + 2; nj < m; nj += 2){
                if (grid[i][nj - 1] == '|'){
                    break;
                }
                else{
                    if (not seen[i][nj]) {
                        if (grid[i][nj] == 'D') {
                            d.erase(make_pair(i, nj));
                        }
                        seen[i][nj] = 2;
                        if (grid[i - 1][nj] == '-' or grid[i + 1][nj] == '-') {
                            q.emplace_back(i, nj);
                        }
                    }
                    else if (seen[i][nj] & 2) {
                        break;
                    }
                    else{
                        seen[i][nj] |= 2;
                    }
                }
            }
        }
        if (grid[i][j + 1] == '|'){
            for (int nj = j - 2; nj > 0; nj -= 2){
                if (grid[i][nj + 1] == '|'){
                    break;
                }
                else{
                    if (not seen[i][nj]) {
                        if (grid[i][nj] == 'D') {
                            d.erase(make_pair(i, nj));
                        }
                        seen[i][nj] = 2;
                        if (grid[i - 1][nj] == '-' or grid[i + 1][nj] == '-') {
                            q.emplace_back(i, nj);
                        }
                    }
                    else if (seen[i][nj] & 2) {
                        break;
                    }
                    else{
                        seen[i][nj] |= 2;
                    }
                }
            }
        }
    }

    for (auto cur: d){
        grid[cur.first][cur.second] = ' ';
    }
    for (int i = 0; i < n; i ++){
        cout << grid[i] << '\n';
    }
    return 0;
}
