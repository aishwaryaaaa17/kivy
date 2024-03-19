 # Import necessary modules from Kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# Define the main layout class for the app
class AttendanceApp(BoxLayout):
    def __init__(self, **kwargs):
        super(AttendanceApp, self).__init__(**kwargs)

        # Add widgets to the layout
        self.orientation = "vertical"

        self.label = Label(text="Welcome to Attendance System", size_hint=(1, 0.5))
        self.add_widget(self.label)

        self.mark_button = Button(text="Mark Attendance", size_hint=(1, 0.2))
        self.mark_button.bind(on_press=self.mark_attendance)
        self.add_widget(self.mark_button)

        self.view_button = Button(text="View Attendance", size_hint=(1, 0.2))
        self.view_button.bind(on_press=self.view_attendance)
        self.add_widget(self.view_button)

    # Define the method to handle marking attendance
    def mark_attendance(self, instance):
        # Implement the logic for marking attendance here
        self.label.text = "Attendance Marked Successfully"

    # Define the method to handle viewing attendance
    def view_attendance(self, instance):
        # Implement the logic for viewing attendance here
        self.label.text = "Viewing Attendance Records"

# Define the main app class
class AttendanceSystemApp(App):
    def build(self):
        return AttendanceApp()

# Run the app
if __name__ == '__main__':
    AttendanceSystemApp().run()
