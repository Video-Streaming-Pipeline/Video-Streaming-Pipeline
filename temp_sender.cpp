#include <glib.h>
#include <glib/gprintf.h>
#include <gst/gst.h>

int main(int argc, char *argv[]){
    //TODO 1. 인풋 스트림을 열어서
    // stream = Gobject.~~~
    // frame = stream.read()
    GstElement *pipeline;
    GError *err = NULL;
    GstBus *bus;
    GMainLoop *loop;
    
    //init GSTREAMER
    gst_init(&argc, &argv);
    loop = g_main_loop_new(NULL, FALSE);

    // setup pipeline
    pipeline = gst_parse_launch("gst-launch-1.0 udpsrc port=9777 ! application/x-rtp ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! autovideosink sync=false", &err);

    // play
    gst_element_set_state(pipeline, GST_STATE_PLAYING);
    bus = gst_element_get_bus(pipeline);
    //gst_bus_add_watch(bus, bus_call, loop);
    g_main_loop_run(loop);

    //clean up
    gst_element_set_state(pipeline, GST_STATE_NULL);
    gst_object_unref(GST_OBJECT(pipeline));
    g_main_loop_unref(loop);
    
    return 0;
}

// #include <gst/gst.h>

// int main(int argc, char * argv[]) {
//     GMainLoop *main_loop;
//     GstElement *pipeline;
//     GstBus *bus;
//     GstMessage *msg;

//     /* Initalize GStreamer */
//     gst_init(&argc, &argv);

//     /* Build the pipeline */
//     pipeline = gst_parse_launch("autovideosrc ! videoscale ! video/x-raw, width=224,height=224 ! videoconvert ! x264enc ! queue ! rtph264pay config-interval=1 pt=96 ! udpsink host=127.0.0.1 port=9191", NULL);

//     main_loop = g_main_loop_new(NULL, FALSE);

//     /* Start playing */
//     gst_element_set_state(pipeline, GST_STATE_PLAYING);
//     g_main_loop_run(main_loop);
//     /* Wait until error or EOS */
//     bus = gst_element_get_bus(pipeline);
//     msg = gst_bus_timed_pop_filtered(bus, GST_CLOCK_TIME_NONE, GST_MESSAGE_ERROR | GST_MESSAGE_EOS);

//     /* Free resources */
//     if (msg != NULL)
//         gst_message_unref(msg);
//     gst_object_unref(bus);
//     gst_element_set_state(pipeline, GST_STATE_NULL);
//     gst_object_unref(pipeline);
//     return 0;
// }
