#!/usr/bin/env node
import { promises as fs } from 'fs'
import puppeteer from 'puppeteer'

const html = await fs.readFile('resume.html', 'utf-8')

const browser = await puppeteer.launch()
const page = await browser.newPage()

await page.setContent(html, { waitUntil: 'networkidle0' })
await page.pdf({ path: 'resume.pdf', format: 'a4', printBackground: true })
await browser.close()
