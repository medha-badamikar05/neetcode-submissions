class LRUCache{
    int capacity = 0;
    unordered_map<int, list<pair<int, int>>::iterator> cache;
    list<pair<int, int>> lru;
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        if(this->cache.find(key) != this->cache.end()) {
            auto it = cache[key];
            int val = cache[key]->second;
            lru.erase(it);
            lru.push_front({key, val});
            cache[key] = lru.begin();
            return val;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if(this->cache.find(key) != this->cache.end()) {
            auto it = cache[key];
            lru.erase(it);
        }
        else if(cache.size() >= capacity) {
            cache.erase(lru.back().first);
            lru.pop_back();
        }
        lru.push_front({key, value});
        cache[key] = lru.begin();
    }
};
