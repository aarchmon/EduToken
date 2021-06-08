# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome to EduToken, my name is Veronica. What can I do for you? "

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CraftonCollegeIntentHandler(AbstractRequestHandler):
    """Handler for CraftonCollegeIntent. """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        
        return ask_utils.is_intent_name("CraftonCollegeIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "With its dedicated professors, ample extracurricular opportunities, supportive staff, and beautiful surroundings, Crafton Hills College is a place where students thrive. "
        speak_output += "CHC offers more than 50 majors in the liberal arts and sciences, vocations, and technical studies, and currently serves about 4,500 students." 
        speak_output += "Professors are experts in their field, and are active in their professions outside of the classroom."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class FallEnrollmentIntentHandler(AbstractRequestHandler):
    """Handler for FallEnrollmentIntent. """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        
        return ask_utils.is_intent_name("FallEnrollmentIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        speak_output = "Depending on your priority level, registration for the Fall 2021 term is open from May 10th through August 15th. "
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class FallStartIntentHandler(AbstractRequestHandler):
    """Handler for FallStartIntent. """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FallStartIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        speak_output = "The Fall 2021 term commences on August 16th. "
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class FinancialAidAvailableIntentHandler(AbstractRequestHandler):
    """Handler for FinancialAidAvailableIntent. """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FinancialAidAvailableIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        speak_output = "For the 2021 and 2022 academic year, financial aid applications opened on October 1st, 2020. "
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class FounderIntentHandler(AbstractRequestHandler):
    """Handler for FounderIntent. """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FounderIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        speak_output = "EduToken was created by Aruna Bisht, Lucas Manning, and Aaron Montano at the UC Berkeley FinTech Bootcamp in June, 2021. "
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class JokeIntentHandler(AbstractRequestHandler):
    """Handler for JokeIntent. """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("JokeIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        speak_output = "I don't mean to brag about my financial skills...but my bank calls me every day to tell me that my debt is outstanding. "
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class OverviewIntentHandler(AbstractRequestHandler):
    """Handler for OverviewIntent. """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("OverviewIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        speak_output = "EduToken is a revolutionary system of redeeming and ensuring educational costs. " 
        speak_output += "Our goal is to ensure that all of your educational needs are properly accounted for."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SummerEnrollmentIntentHandler(AbstractRequestHandler):
    """Handler for SummerEnrollmentIntent. """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SummerEnrollmentIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        speak_output = "Depending on your priority level, enrollment for the 2021 Summer term begins on April 12th, and ends on May 31st. " 
        speak_output += "Please visit the Crafton Hills College Admissions page to determine your priority level."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SummerSchoolStartIntentHandler(AbstractRequestHandler):
    """Handler for SummerSchoolStartIntent. """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SummerSchoolStartIntent")(handler_input)
    
    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        speak_output = "Summer classes begin June 1st, June 14th, and July 6th. "
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(CraftonCollegeIntentHandler())
sb.add_request_handler(FallEnrollmentIntentHandler())
sb.add_request_handler(FallStartIntentHandler())
sb.add_request_handler(FinancialAidAvailableIntentHandler())
sb.add_request_handler(FounderIntentHandler())
sb.add_request_handler(JokeIntentHandler())
sb.add_request_handler(OverviewIntentHandler())
sb.add_request_handler(SummerEnrollmentIntentHandler())
sb.add_request_handler(SummerSchoolStartIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
