#include <stdio.h>
using namespace std;
 
int main()
{
	int i, j, k, n, knight[100005];
	bool fortune;
	scanf("%d", &n);
	for (i = 0; i < n; ++i)
		scanf("%d", &knight[i]);
	if (n <= 5)
	{
		fortune = true;
		for (i = 0; i < n; ++i)
			if (!knight[i])
				fortune = false;
		if (fortune)
			printf("YES\n");
		else
			printf("NO\n");
	}
	else
	{
		fortune = false;
		for (i = 1; i <= n; ++i)
		{
			if ((n/i) < 3)
				break;
			if (((n/i) >= 3) && ((n%i) == 0))
			{
				for (j = 0; j < i; ++j)
				{
					fortune = true;
					for (k = j; k < n; k += i)
						if (!knight[k])
						{
							fortune = false;
							break;
						}
					if (fortune)
					{
						printf("YES\n");
						break;
					}
				}
			}
			if (fortune)
				break;
		}
		if (!fortune)
			printf("NO\n");
	}
	return 0;
}