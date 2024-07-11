-- List bands with Glam rock as their main style, ranked by their longevity in years until 2022
SELECT
    band_name,
    CASE
        WHEN formed > 0 AND split > 0 THEN (2022 - formed) - (2022 - split)
        WHEN formed > 0 AND split = 0 THEN 2022 - formed
        ELSE 0
    END AS lifespan
FROM
    metal_bands
WHERE
    main_style = 'Glam rock'
ORDER BY
    lifespan DESC;
