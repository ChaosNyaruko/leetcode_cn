class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<pair<int,int>> bars;
        vector<vector<int>> res;
        multiset<int> h;
        for(auto& obj : buildings){
            bars.push_back({obj[0], -obj[2]});
            bars.push_back({obj[1], obj[2]});
        }
        sort(bars.begin(), bars.end());
        h.insert(0);
        int cur = 0, pre = 0;
        for(auto& obj : bars){
            if(obj.second < 0)
                h.insert(-obj.second);
            else
                h.erase(h.find(obj.second));
            cur = *h.rbegin();
            if(cur != pre){
                res.push_back({obj.first, cur});
                pre = cur;
            }
        }
        return res;
    }
};
