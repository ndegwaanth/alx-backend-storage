-- ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT origin, SUM(fans) as nb_fans FROM metal_bands WHERE fans > 0 GROUP BY origin ORDER BY nb_fans DESC;