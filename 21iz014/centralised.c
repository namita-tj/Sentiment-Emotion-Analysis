#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_RESOURCES 100
#define MAX_PROCESSES 100

typedef struct { int id, site, heldBy; } Resource;
typedef struct { int id; Resource *holding, *waiting; } Process;

bool detectCycle(Process* p, Resource* r, Process* c, int s) {
    return c->waiting && (c->waiting->id == p->holding->id) &&
           ((c->id == s) || detectCycle(p, r, &p[c->waiting->heldBy], s));
}

bool checkDeadlockSite(Process* p, Resource* r, int s, int n) {
    for (int i = 0; i < n; i++) {
        if (p[i].id != -1 && p[i].holding && p[i].waiting &&
            p[i].holding->site == s && p[i].waiting->site == s &&
            detectCycle(p, r, &p[i], p[i].id))
            return true;
    }
    return false;
}

bool checkDeadlock(Process* p, Resource* r, int n) {
    for (int i = 0; i < n; i++) {
        if (p[i].waiting && detectCycle(p, r, &p[i], p[i].id)) {
            for (int j = 0; j < n; j++) {
                if (p[j].id != -1 && p[j].holding && p[j].waiting &&
                    (p[j].holding->site != p[j].waiting->site))
                    return true;
            }
            return false;
        }
    }
    return false;
}

int main() {
    Resource r[MAX_RESOURCES];
    Process p[MAX_PROCESSES] = {0};
    int ns, tr = 0;

    printf("Enter the number of sites: ");
    scanf("%d", &ns);

    for (int i = 0; i < MAX_PROCESSES; i++) p[i].id = -1;

    for (int s = 1, nr; s <= ns; s++) {
        printf("No. of resources in site %d: ", s);
        scanf("%d", &nr);
        for (int i = 0; i < nr; i++) r[tr++] = (Resource){.id = tr, .site = s, .heldBy = -1};
    }

    printf("\nEnter number of processes: ");
    for (int i = 0, h, w, nr; i < MAX_PROCESSES; i++) {
        printf("\nResources held/waited for by process-%d (-1 for none): ", i);
        scanf("%d %d", &h, &w);
        p[i] = (Process){.id = i, .holding = (h != -1 && h < tr) ? &r[h] : NULL, .waiting = (w != -1 && w < tr) ? &r[w] : NULL};
        if (p[i].holding) r[h].heldBy = i;
    }

    bool gd = checkDeadlock(p, r, MAX_PROCESSES);
    bool sd[ns];

    for (int i = 0; i < ns; i++) sd[i] = checkDeadlockSite(p, r, i + 1, MAX_PROCESSES);

    printf("\n%s in central coordinator\n", gd ? "Deadlock detected" : "No deadlock detected");
    for (int i = 0; i < ns; i++)
        printf("%s in site %d\n", sd[i] ? "Deadlock detected" : "No deadlock detected", i + 1);

    return 0;
}
