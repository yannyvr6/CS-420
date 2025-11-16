"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
const vscode_1 = require("vscode");
const TS_EXT_ID = 'vscode.typescript-language-features';
const ESLINT_EXT_ID = 'dbaeumer.vscode-eslint';
const THIS_EXT_NAME = 'vscode-auto-restart-typescript-eslint-servers';
const THIS_EXT_ID = `neotan.${THIS_EXT_NAME}`;
const THIS_EXT_CONFIG_PREFIX = `autoRestart`; // i.e. Configuration `section`
let tsWatcher;
let eslintWatcher;
function activate(context) {
    vscode_1.workspace.onDidChangeConfiguration((e) => {
        // Re-initiate the watchers might be overkill when any configuration 
        // changed, but it's the easiest way to make sure the watchers are 
        // up-to-date with the latest configuration.
        if (e.affectsConfiguration(THIS_EXT_CONFIG_PREFIX)) {
            tsWatcher?.dispose();
            eslintWatcher?.dispose();
            if (getConfig('monitorFilesForTypescript')) {
                tsWatcher = initWatcher('Typescript', restartTsServer);
            }
            if (getConfig('monitorFilesForESLint')) {
                eslintWatcher = initWatcher('ESLint', restartEslintServer);
            }
        }
    });
    if (getConfig('monitorFilesForTypescript')) {
        tsWatcher = initWatcher('Typescript', restartTsServer);
    }
    if (getConfig('monitorFilesForESLint')) {
        eslintWatcher = initWatcher('ESLint', restartEslintServer);
    }
}
exports.activate = activate;
function deactivate() {
    tsWatcher?.dispose();
    eslintWatcher?.dispose();
    console.log(`Extension ${THIS_EXT_ID} is now deactivated!`);
}
exports.deactivate = deactivate;
// ===== Utils =====
function getConfig(property) {
    return vscode_1.workspace.getConfiguration(THIS_EXT_CONFIG_PREFIX).get(property);
}
function restartTsServer() {
    const tsExtension = vscode_1.extensions.getExtension(TS_EXT_ID);
    if (!tsExtension || tsExtension.isActive === false) {
        vscode_1.window.showErrorMessage(`${THIS_EXT_NAME} is not active or not running.`);
        return;
    }
    return vscode_1.commands.executeCommand("typescript.restartTsServer");
}
function restartEslintServer() {
    const eslintExtension = vscode_1.extensions.getExtension(ESLINT_EXT_ID);
    if (!eslintExtension || eslintExtension.isActive === false) {
        vscode_1.window.showErrorMessage("ESLint extension is not active or not running.");
        return;
    }
    return vscode_1.commands.executeCommand("eslint.restart");
}
function initWatcher(extension, cb) {
    let globs = getConfig(`fileGlobFor${extension}`);
    // Compatibility with older configuration format
    if (!Array.isArray(globs)) {
        globs = [globs];
    }
    function createEventHandler(type) {
        return async (e) => {
            const filePath = e.path || e.fsPath;
            try {
                await cb();
                if (getConfig(`showRestartNotificationFor${extension}`)) {
                    vscode_1.window.showInformationMessage(`${extension} Server Restarted as file(s) ${type}: ${filePath}`);
                }
            }
            catch (err) {
                throw new Error(`Failed to restart server when the file "${filePath}" was ${type}`, { cause: err });
            }
        };
    }
    const watchers = globs.map(glob => {
        const watcher = vscode_1.workspace.createFileSystemWatcher(glob, false, false, false);
        watcher.onDidCreate(createEventHandler('created'));
        watcher.onDidChange(createEventHandler('changed'));
        watcher.onDidDelete(createEventHandler('deleted'));
        return watcher;
    });
    return vscode_1.Disposable.from(...watchers);
}
//# sourceMappingURL=extension.js.map