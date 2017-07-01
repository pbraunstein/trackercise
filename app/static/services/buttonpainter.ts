/**
 * Helper class that changes the color of bootstrap buttons. This can be used to signal success or failure
 * to the user
 */
export class ButtonPainter {
    public static BUTTON_PAINT_DELAY_MS: number = 2000;  // delay change for better UX

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

    public static disableButton(buttonId: string): void {
        $(buttonId).addClass('disabled');
        $(buttonId).prop('disabled', true);
    }

    public static enableButton(buttonId: string): void {
        $(buttonId).removeClass('disabled');
        $(buttonId).prop('disabled', false);
    }

    private static removeBootstrapButtonClasses(buttonId: string): void {
        $(buttonId).removeClass('btn-warning').removeClass('btn-success').removeClass('btn-danger');
    }
}
