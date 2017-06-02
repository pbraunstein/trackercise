
export class ButtonPainter {
    public static BUTTON_PAINT_DELAY_MS: number = 2000;

    public static paintButtonGreen(buttonId: string): void {
        ButtonPainter.removeBootstrapButtonClasses(buttonId);
        $(buttonId).addClass('btn-success');
    }

    public static paintButtonYellow(buttonId: string): void {
        ButtonPainter.removeBootstrapButtonClasses(buttonId);
        $(buttonId).addClass('btn-warning');
    }

    public static paintButtonRed(buttonId: string): void {
        ButtonPainter.removeBootstrapButtonClasses(buttonId);
        $(buttonId).addClass('btn-danger');
    }

    private static removeBootstrapButtonClasses(buttonId: string): void {
        $(buttonId).removeClass('btn-warning').removeClass('btn-success').removeClass('btn-danger');
    }
}
