from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start_r = start_c = -1
        litter_map = {}
        litter_count = 0
        
        # Parse the grid
        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    start_r, start_c = r, c
                elif cell == 'L':
                    litter_map[(r, c)] = litter_count
                    litter_count += 1
                    
        # If there's no litter to collect, moves needed = 0
        if litter_count == 0:
            return 0
            
        full_mask = (1 << litter_count) - 1
        
        # Check initial cell if starting on litter/reset
        initial_mask = 0
        if (start_r, start_c) in litter_map:
            initial_mask |= (1 << litter_map[(start_r, start_c)])
            
        if initial_mask == full_mask:
            return 0

        # best_energy[r][c][mask] stores max energy recorded
        best_energy = [[[-1] * (1 << litter_count) for _ in range(n)] for _ in range(m)]
        best_energy[start_r][start_c][initial_mask] = energy
        
        queue = deque([(start_r, start_c, initial_mask, energy, 0)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c, mask, e, steps = queue.popleft()
            
            # If no energy left to move forward
            if e == 0:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries and obstacles
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    ne = e - 1
                    nmask = mask
                    cell = classroom[nr][nc]
                    
                    # Update mask if visiting new litter
                    if cell == 'L' and (nr, nc) in litter_map:
                        nmask |= (1 << litter_map[(nr, nc)])
                        
                    # Check win condition
                    if nmask == full_mask:
                        return steps + 1
                        
                    # Reset energy if visiting reset station
                    if cell == 'R':
                        ne = energy
                        
                    # Prune if this state reached with less/equal energy
                    if ne > best_energy[nr][nc][nmask]:
                        best_energy[nr][nc][nmask] = ne
                        queue.append((nr, nc, nmask, ne, steps + 1))
                        
        return -1