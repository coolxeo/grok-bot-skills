#!/usr/bin/env node
import { readFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

const skills = JSON.parse(readFileSync(new URL('../upstream-skills.json', import.meta.url), 'utf8'));
const args = process.argv.slice(2);
const separator = args.indexOf('--');
const options = separator < 0 ? args : args.slice(0, separator);
const forwarded = separator < 0 ? [] : args.slice(separator + 1);
const dryRun = options.includes('--dry-run');
const names = options.filter(arg => arg !== '--dry-run');

if (names.length !== 1 || (names[0] !== 'all' && !Object.hasOwn(skills, names[0]))) {
  console.error(`Usage: node scripts/install-upstream.mjs <${Object.keys(skills).join('|')}|all> [--dry-run] [-- CLI options]`);
  process.exit(1);
}

// Keep the selected source and skill fixed. Allow destination and listing options only.
const valueOptions = new Set(['--agent', '-a']);
const flagOptions = new Set(['--global', '-g', '--yes', '-y', '--copy', '--list', '-l']);
for (let i = 0; i < forwarded.length; i++) {
  if (valueOptions.has(forwarded[i])) {
    if (!forwarded[i + 1] || forwarded[i + 1].startsWith('-')) {
      console.error('Each --agent option needs one agent name. Repeat it for more agents.');
      process.exit(1);
    }
    i++;
  } else if (!flagOptions.has(forwarded[i])) {
    console.error(`Unsupported option: ${forwarded[i]}`);
    process.exit(1);
  }
}

const selected = names[0] === 'all' ? Object.values(skills) : [skills[names[0]]];
for (const skill of selected) {
  const command = ['--yes', 'skills@1.6.0', 'add', skill.source, '--skill', skill.name, ...forwarded];
  console.log(['npx', ...command].map(arg => JSON.stringify(arg)).join(' '));
  if (dryRun) continue;
  const result = spawnSync('npx', command, { stdio: 'inherit', shell: false });
  if (result.error) console.error(result.error.message);
  if (result.status !== 0) process.exit(result.status ?? 1);
}
