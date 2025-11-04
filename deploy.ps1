# deploy.ps1 - Deploy Pelican site to GitHub Pages

Write-Host "Regenerating site with production settings..." -ForegroundColor Green
pelican content -s publishconf.py

if ($LASTEXITCODE -eq 0) {
    Write-Host "Deploying to gh-pages..." -ForegroundColor Green
    ghp-import -b gh-pages -f -p output
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Committing source changes to main..." -ForegroundColor Green
        git add .
        git commit -m "Update site"
        git push origin main
        
        Write-Host "Deployment complete!" -ForegroundColor Green
        Write-Host "Your site will be live at https://pauboncompte.me in 1-2 minutes" -ForegroundColor Cyan
    } else {
        Write-Host "Error deploying to gh-pages" -ForegroundColor Red
    }
} else {
    Write-Host "Error generating site" -ForegroundColor Red
}