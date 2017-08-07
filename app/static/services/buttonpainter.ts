/**
 * Helper class that changes the color of bootstrap buttons. This can be used to signal success or failure
 * to the user
 */
export class ButtonPainter {
    public static BUTTON_PAINT_DELAY_MS: number = 2000;  // delay change for better UX

    public static handleFormSubmitProcessing(buttonId: string): void {
        ButtonPainter.paintButtonYellow(buttonId);
        ButtonPainter.disableButton(buttonId);
    }

    public static handleFormSubmitSuccess(form: any, buttonId: string): void {
        setTimeout(
            () => {
                ButtonPainter.paintButtonGreen(buttonId);
                ButtonPainter.enableButton(buttonId);
                form.reset();
            },
            ButtonPainter.BUTTON_PAINT_DELAY_MS
        );
    }

    public static handleFormSubmitFailure(buttonId: string): void {
        setTimeout(
            () => {
                ButtonPainter.paintButtonRed(buttonId);
                ButtonPainter.enableButton(buttonId);
            },
            ButtonPainter.BUTTON_PAINT_DELAY_MS
        );
    }

    private static paintButtonGreen(buttonId: string): void {
        ButtonPainter.removeBootstrapButtonClasses(buttonId);
        $(buttonId).addClass('btn-success');
    }

    private static paintButtonYellow(buttonId: string): void {
        ButtonPainter.removeBootstrapButtonClasses(buttonId);
        $(buttonId).addClass('btn-warning');
    }

    private static paintButtonRed(buttonId: string): void {
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
